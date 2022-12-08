from django.urls import path
from compra.views import *

urlpatterns = [
    path("Inicio/", Inicio, name= "compra-inicio"),
    path("Automovil/", Automovil, name= "compra-automovil"),
    path("Clientes/", Clientes, name= "compra-clientes"),
    
    path("automovil/", AutomovilList.as_view(), name= "compra-automovil"),
    path("automovil/detalle/<pk>/", AutomovilDetail.as_view(), name= "compra-automovil-detail"),
    path("automovil/crear/", AutomovilCreate.as_view(), name= "compra-automovil-create"),
    path("automovil/actualizar/<pk>/", AutomovilUpdate.as_view(), name= "compra-automovil-update"),
    path("automovil/borrar/<pk>/", AutomovilDelete.as_view(), name= "compra-automovil-delete")
]