from django.urls import path
from .views import *


urlpatterns = [
    path('criarplanta/', criarPlanta, name='criarPlanta'),
    path('listarplanta/', listPlanta, name='listPlanta'),
    path('editar/<int:id>/', editar, name='editarPlanta'),
    path('deletar/<int:id>', deletar, name='deletarPlanta'),
    
]