from django.urls import path
from venta.views import *

urlpatterns = [
    path("Inicio/", Inicio),
    path("Automovil/", Automovil),
    path("Clientes/", Clientes),
    path("Seguro/", Seguro)
]