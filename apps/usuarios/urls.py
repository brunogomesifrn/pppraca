from django.urls import path
from .views import *


urlpatterns = [
    path('criarusuario/', criarUsuario, name='criarUsuario'),
    path('listarusuario/', listUsuario, name='listUsuario'),
    path('editar/<int:id>/', editar, name='editarUsuario'),
    path('deletar/<int:id>', deletar, name='deletarUsuario'),
    
]