from django.urls import path
from venta.views import *

urlpatterns = [
    path("", Inicio, name= "venta-inicio"),



    path("automovil/crear/", AutomovilCreate.as_view(), name= "venta-automovil"),

    path("Auto_Buscado/", Auto_BuscadoList.as_view(), name= "venta-Auto_Buscado"),
    path("Auto_Buscado/detalle/<pk>/", Auto_BuscadoDetail.as_view(), name= "venta-Auto_Buscado-detail"),
    path("Auto_Buscado/actualizar/<pk>/", Auto_BuscadoUpdate.as_view(), name= "venta-Auto_Buscado-update"),
    path("Auto_Buscado/borrar/<pk>/", Auto_BuscadoDelete.as_view(template_name="venta/Auto_Buscado_confirm_delete.html" ), name= "venta-Auto_Buscado-delete"),

]