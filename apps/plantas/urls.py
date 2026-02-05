from django.urls import path
from .views import *


urlpatterns = [
    path('criarplanta/', criarPlanta, name='criarPlanta'),
    path('listarplanta/', listPlanta, name='listPlanta'),
    path('editarfamilia/<int:id>/', editarPlanta, name='editarPlanta'),
    path('deletarfamilia/<int:id>/', deletarPlanta, name='deletarPlanta'),
    
    path('criarfamilia/', criarFamilia, name='criarFamilia'),
    path('listarfamilia/', listFamilia, name='listFamilia'),
    path('editarfamilia/<int:id>/', editarFamilia, name='editarFamilia'),
    path('deletarfamilia/<int:id>/', deletarFamilia, name='deletarFamilia'),
]