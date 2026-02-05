from django.shortcuts import render, redirect
from .models import Planta, Familia, FotosPlanta
from apps.core.forms import PlantaForm, FamiliaForm, FotosPlantaForm
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

# FUNÇÃO PARA LISTAR AS FOTOS DAS PLANTAS
def listFotosPlanta(request):
    lista_fotos = FotosPlanta.objects.select_related("planta").all()
    context = {
        "lista_fotos": lista_fotos
    }
    return render(request, "listar_foto.html", context)

# FUNÇÃO PARA CRIAR AS FOTOS DAS PLANTAS
def criar_foto(request):
    form = FotosPlantaForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect("listFotosPlanta")

    context = {
        "form": form
    }
    return render(request, "criar_foto.html", context)

# FUNÇÃO PARA EDITAR AS FOTOS DAS PLANTAS
def editarFotosPlanta(request, id):
    foto = FotosPlanta.objects.get(pk=id)

    form = FotosPlantaForm(request.POST or None, request.FILES or None, instance=foto)
    if form.is_valid():
        form.save()
        return redirect("listFotosPlanta")

    context = {
        "form": form
    }
    return render(request, "criar_foto.html", context)

# FUNÇÃO PARA DELETAR AS FOTOS DAS PLANTAS
def deletarFotosPlanta(request, id):
    foto = FotosPlanta.objects.get(pk=id)
    foto.delete()
    return redirect("listFotosPlanta")