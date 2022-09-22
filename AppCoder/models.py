from django.db import models

# Create your models here. 
# Aca creo un modelo base de datos

class Cursos(models.Model):
    #hereda de model lo que necesita
    nombre=models.CharField(max_length=60)
    camada=models.IntegerField()

class Productos(models.Model):
    #hereda de model lo que necesita
    nombre=models.CharField(max_length=60)
    marca=models.CharField(max_length=60)

class Turnos (models.Model):
    servicio= models.CharField(max_length=60)
    nombre= models.CharField(max_length=60)
    fechaTurno= models.DateField()
