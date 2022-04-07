# fact-crontab-api
É uma api que disponibiliza fatos sobre gatos e/ou felinos. Utilizando tarefas em background, a sua base de dados é populado a partir da API Original [Cat Fact API](https://catfact.ninja/), a qual é o modelo para essa. No entando difereante da API original, que disponibiliza os textos em Inglês, essa api disponiliza os textos em Português, traduzidos a partir de bibliotecas de terceiros.

Para as tarefas em background foi utilizada a biblioteca `django-crontab`, onde sua configuração é bem simples, registrar nos `INSTALLED_APPS` 
```python
INSTALLED_APPS = (
    'django_crontab',
)
```
definir no `settings.py` o periodo de tempo que a tarefa irá executar, nesse caso a cada 2 minutos.
```python
CRONJOBS = [
    ('*/2 * * * *', 'myapp.cron.my_scheduled_job')
]
```
e a função que será executada, que deverá ser criada no arquivo `cron.py` em um app, neste caso dentro do app `task`.
```python
def my_scheduled_job():
    pass
```

### Frameworks e Bibliotecas
- [django-crontab](https://pypi.org/project/django-crontab/)
- [Django REST framawork](https://www.django-rest-framework.org/)
- [Django](https://www.djangoproject.com/)
- [Translate](https://pypi.org/project/translate/)
- [Requests](https://docs.python-requests.org/en/latest/)