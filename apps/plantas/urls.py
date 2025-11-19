from django.urls import path
from . import views


urlpatterns = [
    path('criarplanta/', views.criarPlanta, name='criarPlanta'),
]