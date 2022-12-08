from django.shortcuts import render
from django.http import HttpResponse
from compra.models import *
from compra.forms import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.

def Inicio (request):
    return render(request, "compra/index.html")

def Automovil(request):
    return render(request, "compra/Automovil.html")

def Clientes(request):
    return render(request, "compra/Clientes.html")

class AutomovilList(ListView):
    model = Rodado
    template_name = "compra/list_automovil.html"

class AutomovilDetail(DetailView):
    model = Rodado
    template_name = "compra/detail_automovil.html"

class AutomovilCreate(CreateView):
    model = Rodado
    success_url = "/compra/automovil/"
    fields = ["marca", "modelo" , "color", "km", "año", "precio", "patente", "vtv_hecha"]

class AutomovilUpdate(UpdateView):
    model = Rodado
    success_url = "/compra/automovil/"
    fields = ["marca", "modelo" , "color", "km", "año", "precio", "patente", "vtv_hecha"]

class AutomovilDelete(DeleteView):
    model = Rodado
    success_url = "/compra/automovil/"