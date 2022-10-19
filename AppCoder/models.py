from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
# Create your models here. 
# Aca creo un modelo base de datos

class Cursos(models.Model):
    def __str__(self):
        return f"Nombre del inscripto - camada : {self.nombre} - {self.camada}"
    #hereda de model lo que necesita
    nombre=models.CharField(max_length=60)
    camada=models.IntegerField()

class Productos(models.Model):
    def __str__(self):
        return f"Nombre del producto - marca : {self.nombre} - {self.marca}"
    #hereda de model lo que necesita
    nombre=models.CharField(max_length=60)
    marca=models.CharField(max_length=60)

class Turnos (models.Model):
    def __str__(self):
        return f"Datos turno : {self.servicio} - {self.fechaTurno}"
    servicio= models.CharField(max_length=60)
    nombre= models.CharField(max_length=60)
    fechaTurno= models.DateField()

class Avatar(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)
