from django.urls import path
from .views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('criarespaco/', criarEspaco, name='criarEspaco'),
    path('listarespaco/', listEspaco, name='listEspaco'),
    path('editarespaco/<int:id>/', editarEspaco, name='editarEspaco'),
    path('deletarespaco/<int:id>/', deletarEspaco, name='deletarEspaco'),

]
