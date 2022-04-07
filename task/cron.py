from .models import Fact
import requests

from .utils import translate

def my_scheduled_job():
  res = requests.get(url='https://catfact.ninja/fact/').json()
  fact = translate(res['fact'])
  exists = Fact.objects.filter(fact=fact).exists()
  if not exists:
    Fact.objects.create(fact=fact)
  
