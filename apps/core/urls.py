from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('acervo/', acervo, name='acervo'),
    path('acontecimentos/', acontecimentos, name="acontecimentos"),
    path('contato/', contato, name='contato'),
    path('espacos/', espacos, name='espacos'),
    path('login/', login, name='login'),
    path('sobre-a-praca/', sobrePraca, name='sobrePraca'),
    path('visitacao/', visitacao, name='visitacao'),
]
