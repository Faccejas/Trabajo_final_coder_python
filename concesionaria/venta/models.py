from django.db import models

# Create your models here.

class Empleados(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    dni = models.CharField(max_length=20)
    domicilio = models.CharField(max_length=50)
    localidad = models.CharField(max_length=20)
    celular = models.IntegerField()
    email= models.EmailField(max_length=50)

    def __str__(self):
        return f"{self.nombre.capitalize()} | {self.apellido.capitalize()} | {self.dni} | {self.domicilio.capitalize()} | {self.localidad.capitalize()} | {self.celular} | {self.email}"

