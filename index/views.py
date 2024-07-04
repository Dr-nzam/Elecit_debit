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
    return render (request, 'register.html')