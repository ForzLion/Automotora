from django.db import models

# Create your models here.

class Marca(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    #este str define el nombre
    #en los listados del admin
    def __str__(self):
        return self.nombre

class Automovil(models.Model):
    patente  = models.CharField(max_length=10, unique=True)
    modelo = models.CharField(max_length=50)
    anio = models.IntegerField()
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.patente


