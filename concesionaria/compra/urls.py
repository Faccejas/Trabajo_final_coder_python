from django.urls import path
from compra.views import *

urlpatterns = [
    path("Inicio/", Inicio),
    path("Automovil/", Automovil),
    path("Clientes/", Clientes)
]