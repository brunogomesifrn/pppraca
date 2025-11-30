from django.shortcuts import render, redirect
from .models import Planta
from apps.core.forms import PlantaForm
# Create your views here.


#FUNÇÃO PARA LISTAR AS PLANTAS
def listPlanta(request):
    listPlanta = Planta.objects.all()
    context = {
        'lista_plantas':listPlanta
    }
    return render(request, 'listar_planta.html', context)

#FUNÇÃO PARA CRIAR AS PLANTAS
def criarPlanta(request):
    form = PlantaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listPlanta')

    context = {
        'form': form
    }
    return render(request, 'criar_planta.html', context)

#FUNÇÃO PARA EDITAR AS PLANTAS
def editar(request, id):
    planta = Planta.objects.get(pk=id)

    form = PlantaForm(request.POST or None, instance=planta)
    if form.is_valid():
        form.save()
        return redirect('listPlanta')
    
    context = {
        'form': form
    }
    return render(request, 'criar_planta.html', context)

#FUNÇÃO PARA DELETAR AS PLANTAS
def deletar(request, id):
    planta = Planta.objects.get(pk=id)
    planta.delete()
    return redirect('listPlanta')