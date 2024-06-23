from django.db import models

# Create your models here.

class Categoria(models.Model):
    id = models.AutoField(primary_key=True) #Clave primaria autogenerada
    nombre = models.CharField(max_length=255)

class Producto(models.Model):
    id = models.AutoField(primary_key=True)  # Clave primaria autogenerada
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    id_categoria =  models.ForeignKey(Categoria , on_delete=models.CASCADE)  # Relación con el modelo Categoria
    marca = models.CharField(max_length=50)
    elaboracion = models.DateField()
    caducidad = models.DateField()
    stock = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} {self.marca}"
    
