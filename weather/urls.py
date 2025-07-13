
from django.urls import path
from . import views

app_name = 'weather'

urlpatterns = [
    path('', views.forecast, name='forecast'),
    path('form/', views.form, name='form'),
]
