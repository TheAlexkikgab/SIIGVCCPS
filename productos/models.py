from django.db import models

# Create your models here.

class Categoria(models.Model):
    id = models.AutoField(primary_key=True) #Clave primaria autogenerada
    nombre = models.CharField(max_length=255)
    
    class Meta:
        ordering = ['nombre'] #Ordenar Alfabéticamente según el nombre (ascendentemente)
    
    def __str__(self):
        return self.nombre

class Marca(models.Model):
    id = models.AutoField(primary_key=True) #Clave primaria autogenerada
    nombre = models.CharField(max_length=255)
    
    class Meta:
        ordering = ['nombre'] #Ordenar Alfabéticamente según el nombre (ascendentemente)
    
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    id = models.AutoField(primary_key=True)  # Clave primaria autogenerada
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(null=True, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria =  models.ForeignKey(Categoria, on_delete=models.CASCADE)  # Relación con el modelo Categoria
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)  # Relación con el modelo Marca
    elaboracion = models.DateField(null=True, blank=True)
    caducidad = models.DateField(null=True, blank=True)
    stock = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['nombre'] #Ordenar Alfabéticamente según el nombre (ascendentemente)

    def __str__(self):
        return self.nombre
