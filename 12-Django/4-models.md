# Que es?

- Son las bdd
- Es necesario crear una app

# models

Para crear cada tabla, crear una clase

ej: 

```
class Articulos(models.Model):
    nombre=models.CharField(max_length=30)
    seccoon=models.CharField(max_length=30)
    precio = models.IntegerField()

class Pedidos(models.Model):
    numero=models.IntegerField()
    fecha=models.DateField()
    entregado=models.BooleanField()
```

Para crear los models

``` 
python manage.py makemigrations
```

para que se creen las tablas automaticamente con django

```
python manage.py sqlmigrate gestionPedidos numero_de_migración 
```

finalmente ejecutar

```
python manage.py migrate
```

NOTA: Django crea automaticamente crea el id y lo pone como llave primaria

REVISAR LAS FUNCIONES QUE EXISTEN