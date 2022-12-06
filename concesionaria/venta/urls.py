from django.urls import path
from venta.views import *

urlpatterns = [
    path("Inicio/", Inicio, name= "venta-inicio"),
    path("Automovil/", Automovil, name= "venta-automovil"),
    path("Clientes/", Clientes, name= "venta-clientes"),
    path("Seguros/", Seguro, name= "venta-seguros")
]