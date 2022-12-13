from django.urls import path
from compra.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", Inicio, name= "compra-inicio"),
    #path("automovil/", Automovil, name= "compra-automovil"),
    #path("clientes/", Clientes, name= "compra-clientes"),
    path("nosotros/", Nosotros, name= "compra-nosotros"),


    path("automovil/", AutomovilList.as_view(), name= "compra-automovil"),
    path("automovil/detalle/<pk>/", AutomovilDetail.as_view(), name= "compra-automovil-detail"),
    path("automovil/crear/", AutomovilCreate.as_view(), name= "compra-automovil-create"),
    path("automovil/actualizar/<pk>/", AutomovilUpdate.as_view(), name= "compra-automovil-update"),
    path("automovil/borrar/<pk>/", AutomovilDelete.as_view(), name= "compra-automovil-delete"),


    path("Auto_Buscado/detalle/<pk>/", Auto_BuscadoDetail.as_view(), name= "compra-Auto_Buscado-detail"),
    path("Auto_Buscado/crear/", Auto_BuscadoCreate.as_view(), name= "compra-Auto_Buscado-create"),
    path("Auto_Buscado/actualizar/<pk>/", Auto_BuscadoUpdate.as_view(), name= "compra-Auto_Buscado-update"),
    path("Auto_Buscado/borrar/<pk>/", Auto_BuscadoDelete.as_view(), name= "compra-Auto_Buscado-delete"),

    path("aseguradora/", AseguradoraList.as_view(), name= "compra-aseguradora"),
    path("aseguradora/detalle/<pk>/", AseguradoraDetail.as_view(), name= "compra-aseguradora-detail"),
    path("aseguradora/crear/", AseguradoraCreate.as_view(), name= "compra-aseguradora-create"),
    path("aseguradora/actualizar/<pk>/", AseguradoraUpdate.as_view(), name= "compra-aseguradora-update"),
    path("aseguradora/borrar/<pk>/", AseguradoraDelete.as_view(), name= "compra-aseguradora-delete"),

    path("login/", iniciar_sesion, name="auth-login"),
    path("register/", registrar_usuario, name="auth-register"),
    path("logout/", LogoutView.as_view(template_name="compra/logout.html" ) , name="auth-logout"),
    path("perfil/editar/", editar_perfil, name="auth-editar-perfil"),
    path("perfil/avatar/", agregar_avatar, name="auth-avatar")

]