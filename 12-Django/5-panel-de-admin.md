# /admin/

Para crear el superusuario que administrará el panel de control se debe crear con el código

```
python manage.py createsuperuser
```

Desde admin se pueden poner los modelos para gestionarlos desde el panel de control

```
from gestionPedidos.models import Clientes, Articulos, Pedidos

admin.site.register(Clientes)
admin.site.register(Articulos)
admin.site.register(Pedidos)
```

Para hacer que un campo sea opcional

```
email=models.EmailField(blank=True, null=True)
```

# ModelAdmin

Permite hacer cambios en los modeles que se trabajan en los modelos de admin

```
class ClientesAdmin(admin.ModelAdmin):
    list_display=("nombre","direccion","telefono")

admin.site.register(Clientes, ClientesAdmin)
```