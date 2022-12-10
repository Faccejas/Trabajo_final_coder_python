from django.urls import path
from venta.views import *

urlpatterns = [
    #path("Inicio/", Inicio, name= "venta-inicio"),
    #path("Automovil/", Automovil, name= "venta-automovil"),
    #path("Clientes/", Clientes, name= "venta-clientes"),
    #path("Seguros/", Seguro, name= "venta-seguros"),

    path("automovil/", AutomovilList.as_view(), name= "venta-automovil"),
    path("automovil/detalle/<pk>/", AutomovilDetail.as_view(), name= "venta-automovil-detail"),
    path("automovil/crear/", AutomovilCreate.as_view(), name= "venta-automovil-create"),
    path("automovil/actualizar/<pk>/", AutomovilUpdate.as_view(), name= "venta-automovil-update"),
    path("automovil/borrar/<pk>/", AutomovilDelete.as_view(), name= "venta-automovil-delete"),

    path("comprador/", CompradorList.as_view(), name= "venta-comprador"),
    path("comprador/detalle/<pk>/", CompradorDetail.as_view(), name= "venta-comprador-detail"),
    path("comprador/crear/", CompradorCreate.as_view(), name= "venta-comprador-create"),
    path("comprador/actualizar/<pk>/", CompradorUpdate.as_view(), name= "venta-comprador-update"),
    path("comprador/borrar/<pk>/", CompradorDelete.as_view(), name= "venta-comprador-delete"),




]