from django.shortcuts import render, redirect

from compra.models import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

#login
from compra.forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


#Pagina de inicio:
def Inicio (request):
    if request.user.is_authenticated:
        if len(Avatar.objects.filter(user= request.user.id))==1:
            imagen_model = Avatar.objects.filter(user= request.user.id).order_by("-id")[0]
            imagen_url = imagen_model.imagen.url
        else:
            imagen_url = ""
    else:
        imagen_url = ""
    return render(request, "compra/inicio.html", {"imagen_url": imagen_url})
def Nosotros (request):
    return render(request, "compra/Nosotros.html")
 


class AutomovilList(ListView):
    model = Rodado
    template_name = "compra/list_automovil.html"

class AutomovilDetail(LoginRequiredMixin, DetailView):
    model = Rodado
    template_name = "compra/detail_automovil.html"

class AutomovilUpdate(LoginRequiredMixin, UpdateView):
    model = Rodado
    success_url = "/compra/automovil/"
    fields = ["marca", "modelo" , "color", "km", "año", "precio", "patente", "vtv_hecha", "nombre_apellido_vendedor", "telefono"]

class AutomovilDelete(LoginRequiredMixin, DeleteView):
    model = Rodado  
    success_url = "/compra/automovil/"


class Auto_BuscadoCreate(LoginRequiredMixin, CreateView):
    model = Auto_Buscado
    success_url = "/venta/Auto_Buscado/"
    fields = [ "marca" , "modelo" , "color" , "nombre_comprador", "apellido" , "dni", "celular", "email"]
    template_name = "compra/Auto_Buscado_form.html"

class Auto_BuscadoDetail(LoginRequiredMixin, DetailView):
    model = Auto_Buscado
    template_name = "compra/detail_Auto_Buscado.html"

class Auto_BuscadoUpdate(LoginRequiredMixin, UpdateView):
    model = Auto_Buscado
    success_url = "/venta/Auto_Buscado/"
    fields = ["nombre", "apellido" , "dni", "domicilio", "localidad", "celular", "email"]

class Auto_BuscadoDelete(LoginRequiredMixin, DeleteView):
    model = Auto_Buscado
    success_url = "/venta/Auto_Buscado/"





#seguros 
class AseguradoraList(ListView):
    model = Aseguradora
    template_name = "compra/list_aseguradora.html"

class AseguradoraDetail(DetailView):
    model = Aseguradora
    template_name = "compra/detail_aseguradora.html"

class AseguradoraCreate(LoginRequiredMixin, CreateView):
    model = Aseguradora
    success_url = "/compra/aseguradora/"
    fields = ["razon_social", "telefono" , "celular", "poliza", "domicilio"]
    template_name = "compra/aseguradora_form.html"
    
class AseguradoraUpdate(LoginRequiredMixin, UpdateView):
    model = Aseguradora
    success_url = "/compra/aseguradora/"
    fields = ["razon_social", "telefono" , "celular", "poliza", "domicilio"]

class AseguradoraDelete(LoginRequiredMixin, DeleteView):
    model = Aseguradora
    success_url = "/compra/aseguradora/"




class MensajesList(LoginRequiredMixin, ListView):
    model = Mensajes
    template_name = "compra/list_mensajes.html"


class MensajesCreate(LoginRequiredMixin, CreateView):
    model = Mensajes
    success_url = "/compra/mensajeria/"
    fields = [ "escritor", 'texto']
    template_name = "compra/mensajes_form.html"
    
class MensajesUpdate(LoginRequiredMixin, UpdateView):
    model = Mensajes
    success_url = "/compra/mensajeria/"
    fields = [ "escritor", 'texto']

class MensajesDelete(LoginRequiredMixin, DeleteView):
    model = Mensajes
    success_url = "/compra/mensajeria/"





#inicio de sesion
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

    
def registrar_usuario(request):

    if request.method == "POST":
        formulario = UserRegisterForm(request.POST)

        if formulario.is_valid():
            
            formulario.save()
            return redirect("auth-avatar")
        else:
            return render(request, "compra/register.html", { "form": formulario, "errors": formulario.errors})

    formulario  = UserRegisterForm()
    return render(request, "compra/register.html", { "form": formulario})

@login_required
def editar_perfil(request):

    usuario = request.user

    if request.method == "POST":
    
        formulario = UserEditForm(request.POST)


        if formulario.is_valid():
            data = formulario.cleaned_data

            usuario.email = data["email"]
            usuario.first_name = data["first_name"]
            usuario.last_name = data["last_name"]

            usuario.save()
            return redirect("compra-inicio")
        else:
            return render(request, "compra/editar_perfil.html", {"form": formulario, "erros": formulario.errors})
    else:
        formulario = UserEditForm(initial = {"email": usuario.email, "first_name": usuario.first_name, "last_name": usuario.last_name})

    return render(request, "compra/editar_perfil.html", {"form": formulario})




@login_required
def agregar_avatar(request):
    
    if request.method == "POST":
        formulario = AvatarForm(request.POST, files=request.FILES)
        
        if formulario.is_valid():
            data = formulario.cleaned_data

            usuario = request.user

            avatar = Avatar(user=usuario, imagen=data["imagen"])
            avatar.save()

            return redirect("compra-inicio")
        else:
            return render(request, "compra/agregar_avatar.html", {"form": formulario, "errors": formulario.errors })
    formulario = AvatarForm()

    return render(request, "compra/agregar_avatar.html", {"form": formulario})