from django.db import models

# Create your models here.
from django.db import models
from clientes.models import Cliente  # Importar el modelo de Cliente
from productos.models import Producto  # Importar el modelo de Producto

class Venta(models.Model):
    id = models.AutoField(primary_key=True)  # Clave primaria autogenerada
    id_cliente = models.ForeignKey(Cliente , on_delete=models.CASCADE)  # Relación con el modelo Cliente
    fecha = models.DateTimeField(auto_now_add=True)  # Fecha de la venta (autogenerada)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    metodo_pago = models.CharField(max_length=50)
    estatus_venta = models.CharField(max_length=50)
    descuento = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    impuestos = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    

class Detalle(models.Model):
    id = models.AutoField(primary_key=True)  # Clave primaria autogenerada
    id_venta = models.ForeignKey(Venta, on_delete=models.CASCADE)  # Relación con el modelo Venta
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)  # Relación con el modelo Producto
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)