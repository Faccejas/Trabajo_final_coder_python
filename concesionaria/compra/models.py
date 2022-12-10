from django.db import models

# Create your models here.


class Vendedor(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    dni = models.CharField(max_length=20)
    domicilio = models.CharField(max_length=50)
    localidad = models.CharField(max_length=20)
    celular = models.IntegerField()
    email= models.EmailField(max_length=50)

    def __str__(self):
        return f"{self.nombre.capitalize()} | {self.apellido.capitalize()} | {self.dni} | {self.domicilio.capitalize()} | {self.localidad.capitalize()} | {self.celular} | {self.email}"

class Rodado(models.Model):
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=50)
    color = models.CharField(max_length=20)
    km = models.CharField(max_length=20)
    año = models.IntegerField()
    precio = models.CharField(max_length=20)
    patente = models.CharField(max_length=20)
    vtv_hecha = models.CharField(max_length=20)
    
    def __str__(self):
        return f"{self.marca.capitalize()} | {self.modelo.capitalize()} | {self.color.capitalize()} | {self.km} | {self.año} | {self.precio} | {self.patente.upper()} | {self.vtv_hecha.capitalize()}"
class Aseguradora(models.Model):
    razon_social = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    celular = models.IntegerField()
    poliza = models.IntegerField()
    domicilio = models.CharField(max_length=50)
    localidad = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.razon_social} | {self.telefono} | {self.celular} | {self.poliza} | {self.domicilio.capitalize()} | {self.localidad.capitalize()}"