from django.db import models

# Create your models here.


class Vendedor(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    dni = models.IntegerField()
    domicilio = models.CharField(max_length=50)
    localidad = models.CharField(max_length=20)
    celular = models.IntegerField()
    email= models.CharField(max_length=50)

class Rodado(models.Model):
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=50)
    color = models.CharField(max_length=20)
    km = models.IntegerField()
    año = models.IntegerField()
    precio = models.IntegerField()
    patente = models.CharField(max_length=20)
    vtv_hecha = models.CharField(max_length=20)
    