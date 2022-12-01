from django.shortcuts import render
from django.http import HttpResponse
from venta.models import *

# Create your views here.

def Inicio (request):
    return render(request, "venta/index.html")
