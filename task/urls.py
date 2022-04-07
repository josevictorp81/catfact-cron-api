from rest_framework.routers import DefaultRouter
from django.urls import path, include

from . import views

router = DefaultRouter()
router.register('facts', views.FactViewSet)
router.register('fact', views.FactRandomViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

