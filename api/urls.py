from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ThoughtViewSet
from . import views

router = DefaultRouter()

router.register(r'thoughts', ThoughtViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('weather/', views.weather_lookup, name='weather_lookup'),
    path('users/', views.user_lookup, name='user_lookup'),
]
