from django.urls import path
from venta.views import *

urlpatterns = [
    path("", Inicio, name= "venta-inicio"),
    #path("Automovil/", Automovil, name= "venta-automovil"),
    #path("Clientes/", Clientes, name= "venta-clientes"),
    #path("Seguros/", Seguro, name= "venta-seguros"),

    #path("automovil/", AutomovilList.as_view(), name= "venta-automovil"),
    #path("automovil/detalle/<pk>/", AutomovilDetail.as_view(), name= "venta-automovil-detail"),
    path("automovil/crear/", AutomovilCreate.as_view(), name= "venta-automovil"),
    path("automovil/actualizar/<pk>/", AutomovilUpdate.as_view(), name= "venta-automovil-update"),
    path("automovil/borrar/<pk>/", AutomovilDelete.as_view(), name= "venta-automovil-delete"),

    path("empleados/", EmpleadosList.as_view(), name= "venta-empleados"),
    path("empleados/detalle/<pk>/", EmpleadosDetail.as_view(), name= "venta-empleados-detail"),
    path("empleados/crear/", EmpleadosCreate.as_view(), name= "venta-empleados-create"),
    path("empleados/actualizar/<pk>/", EmpleadosUpdate.as_view(), name= "venta-empleados-update"),
    path("empleados/borrar/<pk>/", EmpleadosDelete.as_view(), name= "venta-empleados-delete"),

    path("Auto_Buscado/", Auto_BuscadoList.as_view(), name= "venta-Auto_Buscado"),


]