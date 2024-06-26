from django.contrib import admin
from .models import Cliente

# Register your models here.
class ClienteAdmin(admin.ModelAdmin):
    list_display = ["cedula", "nombres", "apellidos", "telefono", "email"]
    search_fields = ("nombres", "apellidos", "cedula")

admin.site.register(Cliente, ClienteAdmin)