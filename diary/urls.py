
from django.urls import path
from . import views

app_name = 'diary'

urlpatterns = [
    path('create/', views.create, name='create'),
    path('thoughts/', views.listed, name='thoughts'),
    path('thoughts/<slug:slug>/', views.view_thought, name='view_thought'),

]
