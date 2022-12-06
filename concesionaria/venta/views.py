from django.shortcuts import render
from django.http import HttpResponse
from venta.models import *

# Create your views here.

def Inicio (request):
    return render(request, "venta/index.html")

def Automovil(request):
    return render(request, "venta/Automovil.html")

def Clientes(request):
    return render(request, "venta/Clientes.html")

def Seguro(request):
    return render(request, "venta/Seguro.html")