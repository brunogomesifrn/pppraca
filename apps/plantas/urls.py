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

    path('criarfoto/', criar_foto, name='criarFotosPlanta'),
    path('listarfoto/', listFotosPlanta, name='listFotosPlanta'),
    path('editarfoto/<int:id>/', editarFotosPlanta, name='editarFotosPlanta'),
    path('deletarfoto/<int:id>/', deletarFotosPlanta, name='deletarFotosPlanta'),
]