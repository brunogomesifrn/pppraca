from django.shortcuts import render, redirect
from .models import Planta
# Create your views here.

def criarPlanta(request):
    if request.method == 'GET':
        return render(request, 'criar_planta.html')
    elif request.method == 'POST':
        nomePopular = request.POST.get('nome_popular')
        nomeCientifico = request.POST.get('nome_cientifico')
    planta = Planta(
        nome_popular=nomePopular,
        nome_cientifico=nomeCientifico,
    )

    planta.save()

    return redirect('criarPlanta')

