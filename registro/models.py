from django.db import models

# Create your models here.

class Usuario(models.Model):
    username = models.CharField(default = "default", max_length = 100)
    password = models.CharField(max_length = 100)

class Servicio(models.Model):
    nombre = models.CharField(max_length = 100)
    descripcion = models.CharField(max_length = 100)