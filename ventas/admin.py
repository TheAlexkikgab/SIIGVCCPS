from django.contrib import admin
from .models import Venta, Detalle

# Register your models here.

admin.site.register(Venta)
admin.site.register(Detalle)