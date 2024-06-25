from django.contrib import admin
from .models import Producto, Categoria, Marca

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion', 'precio', 'categoria', 'marca', 'elaboracion', 'caducidad', 'stock']

admin.site.register(Producto, ProductoAdmin)
admin.site.register(Categoria)
admin.site.register(Marca)