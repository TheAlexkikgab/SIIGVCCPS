from django.db import models

# Create your models here.
class Productos(models.Model):
    id = models.AutoField(primary_key=True)  # Clave primaria autogenerada
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    elaboracion = models.DateField()
    caducidad = models.DateField()
    stock = models.IntegerField()

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"