from django.contrib import admin
from .models import Producto, Categoria, Marca

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion', 'precio', 'categoria', 'marca', 'elaboracion', 'caducidad', 'stock']
    search_fields = ['nombre']
    list_filter = ['categoria','marca']

class MarcaAdmin(admin.ModelAdmin):
    search_fields = ['nombre']

class CategoriaAdmin(admin.ModelAdmin):
    search_fields = ['nombre']

admin.site.register(Producto, ProductoAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Marca, MarcaAdmin)