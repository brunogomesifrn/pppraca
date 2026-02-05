from django.shortcuts import render, redirect
from .models import Planta, Familia
from apps.core.forms import PlantaForm, FamiliaForm
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
def editarPlanta(request, id):
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
def deletarPlanta(request, id):
    planta = Planta.objects.get(pk=id)
    planta.delete()
    return redirect('listPlanta')

# FUNÇÃO PARA CRIAR AS FAMÍLIAS
def criarFamilia(request):
    form = FamiliaForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('listFamilia')

    context = {
        'form': form
    }
    return render(request, 'criar_familia.html', context)

# FUNÇÃO PARA LISTAR AS FAMÍLIAS
def listFamilia(request):
    listFamilia = Familia.objects.all()
    context = {
        'lista_familias': listFamilia
    }
    return render(request, 'listar_familia.html', context)

# FUNÇÃO PARA EDITAR AS FAMÍLIAS
def editarFamilia(request, id):
    familia = Familia.objects.get(pk=id)

    form = FamiliaForm(request.POST or None, request.FILES or None, instance=familia)

    if form.is_valid():
        form.save()
        return redirect('listFamilia')

    context = {
        'form': form
    }
    return render(request, 'criar_familia.html', context)

# FUNÇÃO PARA DELETAR AS FAMÍLIAS
def deletarFamilia(request, id):
    familia = Familia.objects.get(pk=id)
    familia.delete()
    return redirect('listFamilia')