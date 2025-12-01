from django.urls import path
from .views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('criarespaco/', criarEspaco, name='criarEspaco'),
    path('listarespaco/', listEspaco, name='listEspaco'),
    path('editar/<int:id>/', editar, name='editarEspaco'),
    path('deletar/<int:id>', deletar, name='deletarEspaco'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)