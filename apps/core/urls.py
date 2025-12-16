from django.urls import path, include
from .views import *
from django.contrib.auth.views import LoginView, LogoutView
from apps.usuarios.views import loginUsuario


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='index'),
    path('acervo/', acervo, name='acervo'),
    path('acontecimentos/', acontecimentos, name="acontecimentos"),
    path('contato/', contato, name='contato'),
    path('espacos/', espacos, name='espacos'),
    # path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('login/', loginUsuario, name='login'),
    path('login/', LogoutView.as_view(), name='logout'), #REVISAR DEPOIS
    # path('login/', login, name='login'),
    path('sobre-a-praca/', sobrePraca, name='sobrePraca'),
    path('visitacao/', visitacao, name='visitacao'),
    path('plantas/', include('apps.plantas.urls')),
    path('espaços/', include('apps.espacos.urls')),
    path('usuarios/', include('apps.usuarios.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)