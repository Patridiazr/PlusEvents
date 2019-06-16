from django.db import models

# Create your models here.

class Usuario(models.Model):
    email = models.EmailField(max_length = 250)
    password = models.CharField(max_length = 100)

class Servicio(models.Model):
    nombre = models.CharField(max_length = 100)
    descripcion = models.CharField(max_length = 100)