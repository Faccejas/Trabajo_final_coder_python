from django.shortcuts import render
from django.http import HttpResponse
from compra.models import *

# Create your views here.

def Inicio (request):
    return render(request, "compra/index.html")

def Automovil(request):
    return render(request, "compra/Automovil.html")

def Clientes(request):
    return render(request, "compra/Clientes.html")