import email
from django.db import models

# Create your models here.

class Clientes(models.Model):
    nombre=models.CharField(max_length=30)
    direccion=models.CharField(max_length=50)
    email=models.EmailField(blank=True, null=True)
    telefono=models.CharField(max_length=15)

class Articulos(models.Model):
    nombre=models.CharField(max_length=30)
    seccoon=models.CharField(max_length=30)
    precio = models.IntegerField()

class Pedidos(models.Model):
    numero=models.IntegerField()
    fecha=models.DateField()
    entregado=models.BooleanField()
