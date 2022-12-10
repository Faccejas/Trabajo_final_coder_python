from django.shortcuts import render
from django.http import HttpResponse
from venta.models import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.

#def Inicio (request):
    #return render(request, "venta/index.html")

#def Automovil(request):
    #return render(request, "venta/Automovil.html")

def Clientes(request):
    return render(request, "venta/Clientes.html")

def Seguro(request):
    return render(request, "venta/Seguro.html")


class AutomovilList(ListView):
    model = Rodado
    template_name = "venta/list_automovil.html"

class AutomovilDetail(DetailView):
    model = Rodado
    template_name = "venta/detail_automovil.html"

class AutomovilCreate(CreateView):
    model = Rodado
    success_url = "/venta/automovil/"
    fields = ["marca", "modelo" , "color", "km", "año", "precio", "patente"]
    template_name = "venta/rodado_form.html"
    
class AutomovilUpdate(UpdateView):
    model = Rodado
    success_url = "/compra/automovil/"
    fields = ["marca", "modelo" , "color", "km", "año", "precio", "patente", "vtv_hecha"]

class AutomovilDelete(DeleteView):
    model = Rodado
    success_url = "/venta/automovil/"