
from django.urls import path
from . import views

app_name = 'weather'

urlpatterns = [
    path('', views.form, name='form'),
    path('forecast/<str:city>/', views.forecast, name='forecast'),
]
