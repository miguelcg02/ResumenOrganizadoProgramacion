from django.contrib import admin
from gestionPedidos.models import Clientes, Articulos, Pedidos

# Register your models here.

class ClientesAdmin(admin.ModelAdmin): # Esto es para el panel de control
    list_display=("nombre","direccion","telefono") # Los campos que se quieren ver
    search_fields=("nombre","telefono") #Barra de busqueda en el ques e puede buscar por estos campos

class ArticulosAdmin(admin.ModelAdmin):
    list_filter=("seccion") #Froma de filtrar

class PedidosAdmin(admin.ModelAdmin):
    list_display=("numero","fecha")
    list_filter=("fecha")
    date_hierarchy="fecha" #aparece un filtro por botones mes a mes y cuando se presiona, día a día

admin.site.register(Clientes, ClientesAdmin)
admin.site.register(Articulos, ArticulosAdmin)
admin.site.register(Pedidos, PedidosAdmin)
