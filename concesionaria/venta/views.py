from django.shortcuts import render
from django.http import HttpResponse
from venta.models import *
from compra.models import Auto_Buscado, Rodado
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.

def Inicio (request):
    return render(request, "venta/inicio.html")

#def Automovil(request):
    #return render(request, "venta/Automovil.html")

#def Clientes(request):
    #return render(request, "venta/Clientes.html")

#def Seguro(request):
    #return render(request, "venta/Seguro.html")


# NO va aca porque no me interesa desde ventas ver que autos tengo class AutomovilList(ListView):
#     model = Rodado
#     template_name = "venta/list_automovil.html"

class AutomovilDetail(DetailView):
    model = Rodado
    template_name = "venta/detail_automovil.html"

class AutomovilCreate(CreateView):
    model = Rodado
    success_url = "/venta/"
    fields = ["marca", "modelo" , "color", "km", "año", "precio", "patente"]
    template_name = "venta/rodado_form.html"
    
class AutomovilUpdate(UpdateView):
    model = Rodado
    success_url = "/venta/"
    fields = ["marca", "modelo" , "color", "km", "año", "precio", "patente"]

class AutomovilDelete(DeleteView):
    model = Rodado
    success_url = "/venta/"



class EmpleadosList(ListView):
    model = Empleados
    template_name = "venta/list_empleados.html"

class EmpleadosDetail(DetailView):
    model = Empleados
    template_name = "venta/detail_empleado.html"

class EmpleadosCreate(CreateView):
    model = Empleados
    success_url = "/venta/empleados/"
    fields = ["nombre", "apellido" , "dni", "domicilio", "localidad", "celular", "email"]
    template_name = "venta/empleados_form.html"
    
class EmpleadosUpdate(UpdateView):
    model = Empleados
    success_url = "/venta/empleados/"
    fields = ["nombre", "apellido" , "dni", "domicilio", "localidad", "celular", "email"]

class EmpleadosDelete(DeleteView):
    model = Empleados
    success_url = "/venta/empleados/"






class Auto_BuscadoList(ListView):
    model = Auto_Buscado
    template_name = "venta/list_Auto_Buscado.html"
