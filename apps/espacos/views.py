from django.shortcuts import render, redirect
from .models import Espaco
from apps.core.forms import EspacoForm
# Create your views here.


#FUNÇÃO PARA LISTAR ESPAÇOS
def listEspaco(request):
    listEspaco = Espaco.objects.all()
    context = {
        'lista_espacos':listEspaco
    }
    return render(request, 'listar_espaco.html', context)

#FUNÇÃO PARA CRIAR ESPAÇOS
def criarEspaco(request):
    form = EspacoForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('listEspaco')

    context = {
        'form': form
    }
    return render(request, 'criar_espaco.html', context)

#FUNÇÃO PARA EDITAR ESPAÇOS
def editar(request, id):
    espaco = Espaco.objects.get(pk=id)

    form = EspacoForm(request.POST or None, request.FILES or None, instance=espaco)
    if form.is_valid():
        form.save()
        return redirect('listEspaco')
    
    context = {
        'form': form
    }
    return render(request, 'criar_espaco.html', context)

#FUNÇÃO PARA DELETAR ESPAÇOS
def deletar(request, id):
    espaco = Espaco.objects.get(pk=id)
    espaco.delete()
    return redirect('listEspaco')