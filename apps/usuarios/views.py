from django.shortcuts import render, redirect
from .models import Usuario
from apps.core.forms import UsuarioForm
# Create your views here.


#FUNÇÃO PARA LISTAR AS USUARIO
def listUsuario(request):
    listUsuario = Usuario.objects.all()
    context = {
        'lista_usuarios':listUsuario
    }
    return render(request, 'listar_usuario.html', context)

#FUNÇÃO PARA CRIAR AS USUARIO
def criarUsuario(request):
    form = UsuarioForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listUsuario')

    context = {
        'form': form
    }
    return render(request, 'criar_usuario.html', context)

#FUNÇÃO PARA EDITAR AS USUARIO
def editar(request, id):
    usuario = Usuario.objects.get(pk=id)

    form = UsuarioForm(request.POST or None, instance=usuario)
    if form.is_valid():
        form.save()
        return redirect('listUsuario')
    
    context = {
        'form': form
    }
    return render(request, 'criar_usuario.html', context)

#FUNÇÃO PARA DELETAR AS USUARIO
def deletar(request, id):
    usuario = Usuario.objects.get(pk=id)
    usuario.delete()
    return redirect('listUsuario')