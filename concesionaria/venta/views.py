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


class AutomovilCreate(LoginRequiredMixin,CreateView):
    model = Rodado
    success_url = "/automovil/"
    fields = ['nombre_apellido_vendedor', 'telefono', "marca", "modelo" , "color", "km", "año", "precio", "patente", "vtv_hecha"]
    template_name = "venta/rodado_form.html"







class Auto_BuscadoList(LoginRequiredMixin, ListView):
    model = Auto_Buscado
    template_name = "venta/list_Auto_Buscado.html"

class Auto_BuscadoDetail(LoginRequiredMixin, DetailView):
    model = Auto_Buscado
    template_name = "venta/detail_Auto_Buscado.html"

class Auto_BuscadoUpdate(LoginRequiredMixin, UpdateView):
    model = Auto_Buscado
    success_url = "/venta/Auto_Buscado/"
    fields = ["nombre_comprador", "apellido" , "dni", "celular", "email", "marca", "modelo", "color"]
    

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