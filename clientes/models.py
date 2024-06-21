from django.db import models

# Create your models here.
class Clientes(models.Model):
    id = models.AutoField(primary_key=True)  # Clave primaria autogenerada
    cedula = models.CharField(max_length=15, unique=True, null=True, blank=True)  # Cédula única (opcional)
    pasaporte = models.CharField(max_length=15, unique=True, null=True, blank=True)  # Pasaporte (opcional)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    nacimiento = models.DateField() #Fecha de nacimiento
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(max_length=255, unique=True)  # Correo electrónico único
 
    def _str_(self):
        return f"{self.nombres} {self.apellidos}"