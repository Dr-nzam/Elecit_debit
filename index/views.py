from django.shortcuts import render

# Create your views here.

def index (request):
    return render(request, 'index/index.html')

def table (request):
    return render(request, 'index/tables.html')

def staticLayout(request):
    return render(request, 'index/layout-static.html')

def charts(request):
    return render(request, 'index/charts.html')

def login (request):
    return render(request, 'index/login.html')

def register (request):
    return render (request, 'index/register.html')

def register_debit (request):
    return render (request, 'index/register-debit.html')

def utilisateurs (request):
    return render (request, 'index/utilisateurs.html')

def historique (request):
    return render (request, 'index/historique.html')

def stocks (request):
    return render (request, 'index/stocks.html')

def changerPassword (request):
    return render (request, 'index/password.html')

def erro401(request):
    return render(request, 'index/401.html')

def erro404 (request):
    return render(request, 'index/404.html')

def erro500 (request):
    return render (request, 'index/500.html')