from django.urls import path
from compra.views import *

urlpatterns = [
    path("Inicio/", Inicio, name= "compra-inicio"),
    path("Automovil/", Automovil, name= "compra-automovil"),
    path("Clientes/", Clientes, name= "compra-clientes")
]