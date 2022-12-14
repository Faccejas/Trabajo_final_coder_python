from django.shortcuts import render, redirect
from django.http import HttpResponse
from venta.models import *
from compra.models import Auto_Buscado, Rodado
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


from compra.forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
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

# No va aca porque esta en compras class AutomovilDetail(DetailView):
    model = Rodado
    template_name = "venta/detail_automovil.html"


class AutomovilCreate(LoginRequiredMixin,CreateView):
    model = Rodado
    success_url = "/venta/"
    fields = ["marca", "modelo" , "color", "km", "año", "precio", "patente"]
    template_name = "venta/rodado_form.html"
    
class AutomovilUpdate(LoginRequiredMixin,UpdateView):
    model = Rodado
    success_url = "/venta/"
    fields = ["marca", "modelo" , "color", "km", "año", "precio", "patente"]

class AutomovilDelete(LoginRequiredMixin,DeleteView):
    model = Rodado
    success_url = "/venta/"



class EmpleadosList(ListView):
    model = Empleados
    template_name = "venta/list_empleados.html"

class EmpleadosDetail(DetailView):
    model = Empleados
    template_name = "venta/detail_empleado.html"

class EmpleadosCreate(LoginRequiredMixin,CreateView):
    model = Empleados
    success_url = "/venta/empleados/"
    fields = ["nombre", "apellido" , "dni", "domicilio", "localidad", "celular", "email"]
    template_name = "venta/empleados_form.html"
    
class EmpleadosUpdate(LoginRequiredMixin,UpdateView):
    model = Empleados
    success_url = "/venta/empleados/"
    fields = ["nombre", "apellido" , "dni", "domicilio", "localidad", "celular", "email"]

class EmpleadosDelete(LoginRequiredMixin,DeleteView):
    model = Empleados
    success_url = "/venta/empleados/"






class Auto_BuscadoList(ListView):
    model = Auto_Buscado
    template_name = "venta/list_Auto_Buscado.html"

class Auto_BuscadoDetail(DetailView):
    model = Auto_Buscado
    template_name = "venta/detail_Auto_Buscado.html"

class Auto_BuscadoCreate(LoginRequiredMixin, CreateView):
    model = Auto_Buscado
    success_url = "/venta/Auto_Buscado/"
    fields = [ "marca" , "modelo" , "color" , "nombre_comprador", "apellido" , "dni", "celular", "email"]
    template_name = "venta/Auto_Buscado_form.html"
    
class Auto_BuscadoUpdate(LoginRequiredMixin, UpdateView):
    model = Auto_Buscado
    success_url = "/venta/Auto_Buscado/"
    fields = ["nombre", "apellido" , "dni", "domicilio", "localidad", "celular", "email"]

class Auto_BuscadoDelete(LoginRequiredMixin, DeleteView):
    model = Auto_Buscado
    success_url = "/venta/Auto_Buscado/"


def iniciar_sesion(request):

    errors = ""

    if request.method == "POST":
        formulario = AuthenticationForm(request, data=request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            user = authenticate(username=data["username"], password=data["password"])
            
            if user is not None:
                login(request, user)
                return redirect ("compra-inicio")
            else:
                return render(request, "compra/login.html", {"form": formulario, "errors": "Credenciales invalidas"})
        else:
            return render(request, "compra/login.html", {"form": formulario, "errors": formulario.errors})
    formulario = AuthenticationForm()
    return render(request, "compra/login.html", {"form": formulario, "errors": errors})