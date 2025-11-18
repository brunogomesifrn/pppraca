from django.shortcuts import render

# Create your views here.
def criar_planta(request):
    return render(request, 'criar_planta.html')