from django.shortcuts import render
from django.http import HttpResponse
from venta.models import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.

#def Inicio (request):
    #return render(request, "venta/index.html")

#def Automovil(request):
    #return render(request, "venta/Automovil.html")

#def Clientes(request):
    #return render(request, "venta/Clientes.html")

#def Seguro(request):
    #return render(request, "venta/Seguro.html")


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
    fields = ["marca", "modelo" , "color", "km", "año", "precio", "patente"]

class AutomovilDelete(DeleteView):
    model = Rodado
    success_url = "/venta/automovil/"



class CompradorList(ListView):
    model = Comprador
    template_name = "venta/list_comprador.html"

class CompradorDetail(DetailView):
    model = Comprador
    template_name = "venta/detail_comprador.html"

class CompradorCreate(CreateView):
    model = Comprador
    success_url = "/venta/comprador/"
    fields = ["nombre", "apellido" , "dni", "domicilio", "localidad", "celular", "email"]
    template_name = "venta/comprador_form.html"
    
class CompradorUpdate(UpdateView):
    model = Comprador
    success_url = "/compra/comprador/"
    fields = ["nombre", "apellido" , "dni", "domicilio", "localidad", "celular", "email"]

class CompradorDelete(DeleteView):
    model = Comprador
    success_url = "/venta/comprador/"



class AseguradoraList(ListView):
    model = Aseguradora
    template_name = "venta/list_aseguradora.html"

class AseguradoraDetail(DetailView):
    model = Aseguradora
    template_name = "venta/detail_aseguradora.html"

class AseguradoraCreate(CreateView):
    model = Aseguradora
    success_url = "/venta/aseguradora/"
    fields = ["razon_social", "telefono" , "celular", "poliza", "domicilio", "localidad"]
    template_name = "venta/aseguradora_form.html"
    
class AseguradoraUpdate(UpdateView):
    model = Aseguradora
    success_url = "/compra/aseguradora/"
    fields = ["razon_social", "telefono" , "celular", "poliza", "domicilio", "localidad"]

class AseguradoraDelete(DeleteView):
    model = Aseguradora
    success_url = "/venta/aseguradora/"