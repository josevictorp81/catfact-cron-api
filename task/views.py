from rest_framework import viewsets
from rest_framework.mixins import ListModelMixin

from .serializers import FactSerializer
from .models import Fact

class FactViewSet(ListModelMixin, viewsets.GenericViewSet):
    serializer_class = FactSerializer
    queryset = Fact.objects.all()
    
    
class FactRandomViewSet(ListModelMixin, viewsets.GenericViewSet):
    serializer_class = FactSerializer
    queryset = Fact.objects.all().order_by('?')[:1]