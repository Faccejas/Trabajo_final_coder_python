from django.shortcuts import render
from django.http import HttpResponse
from compra.models import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.

def Inicio (request):
    return render(request, "compra/inicio.html")

#def Automovil(request):
#    return render(request, "compra/Automovil.html")

#def Clientes(request):
    #return render(request, "compra/Clientes.html")

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
    template_name = "compra/rodado_form.html"
    
class AutomovilUpdate(UpdateView):
    model = Rodado
    success_url = "/compra/automovil/"
    fields = ["marca", "modelo" , "color", "km", "año", "precio", "patente", "vtv_hecha"]

class AutomovilDelete(DeleteView):
    model = Rodado
    success_url = "/compra/automovil/"



class Auto_BuscadoList(ListView):
    model = Auto_Buscado
    template_name = "compra/list_Auto_Buscado.html"

class Auto_BuscadoDetail(DetailView):
    model = Auto_Buscado
    template_name = "compra/detail_Auto_Buscado.html"

class Auto_BuscadoCreate(CreateView):
    model = Auto_Buscado
    success_url = "/compra/Auto_Buscado/"
    fields = [ "marca" , "modelo" , "color" , "nombre_comprador", "apellido" , "dni", "celular", "email"]
    template_name = "compra/Auto_Buscado_form.html"
    
class Auto_BuscadoUpdate(UpdateView):
    model = Auto_Buscado
    success_url = "/compra/Auto_Buscado/"
    fields = ["nombre", "apellido" , "dni", "domicilio", "localidad", "celular", "email"]

class Auto_BuscadoDelete(DeleteView):
    model = Auto_Buscado
    success_url = "/compra/vendedor/"




#aseguradora 
class AseguradoraList(ListView):
    model = Aseguradora
    template_name = "compra/list_aseguradora.html"

class AseguradoraDetail(DetailView):
    model = Aseguradora
    template_name = "compra/detail_aseguradora.html"

class AseguradoraCreate(CreateView):
    model = Aseguradora
    success_url = "/compra/aseguradora/"
    fields = ["razon_social", "telefono" , "celular", "poliza", "domicilio", "localidad"]
    template_name = "compra/aseguradora_form.html"
    
class AseguradoraUpdate(UpdateView):
    model = Aseguradora
    success_url = "/compra/aseguradora/"
    fields = ["razon_social", "telefono" , "celular", "poliza", "domicilio", "localidad"]

class AseguradoraDelete(DeleteView):
    model = Aseguradora
    success_url = "/compra/aseguradora/"