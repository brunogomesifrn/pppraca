from django.shortcuts import render
# Create your views here.

def index(request):
    return render(request, 'index.html')

def acervo(request):
    return render(request, 'acervo.html')

def acontecimentos(request):
    return render(request, 'acontecimentos.html')

def contato(request):
    return render(request, 'contato.html')

def espacos(request):
    return render(request, 'espacos.html')

def login(request):
    return render(request, 'login.html')

def sobrePraca(request):
    return render(request, 'sobre-praca.html')

def visitacao(request):
    return render(request, 'visitacao.html')