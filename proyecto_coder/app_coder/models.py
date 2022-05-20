import email
from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=40) 
    camada = models.IntegerField()
    
class Estudiante(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField(max_length=50)
    activo=models.BooleanField(default=True)

class Profesor(models.Model):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    email=models.EmailField(max_length=50)
    
    