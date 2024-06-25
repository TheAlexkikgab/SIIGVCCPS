from django.db import models
from clientes.models import Cliente  # Importar el modelo de Cliente
from productos.models import Producto  # Importar el modelo de Producto

class Venta(models.Model):
    id = models.AutoField(primary_key=True)  # Clave primaria autogenerada
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)  # Relación con el modelo Cliente
    fecha = models.DateTimeField(auto_now_add=True)  # Fecha de la venta (autogenerada)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    metodo_pago = models.CharField(max_length=50)
    estatus_venta = models.CharField(max_length=50)
    descuento = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    impuestos = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Venta {self.id} - {self.cliente.nombre}"  # Asegúrate de que Cliente tenga un campo nombre
    

class Detalle(models.Model):
    id = models.AutoField(primary_key=True)  # Clave primaria autogenerada
    id_venta = models.ForeignKey(Venta, on_delete=models.CASCADE)  # Relación con el modelo Venta
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)  # Relación con el modelo Producto
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Detalle {self.id} - Venta {self.id_venta.id} - Producto {self.id_producto.nombre}"  # Asegúrate de que Producto tenga un campo nombre


class Carrito(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Carrito {self.id} - {self.cliente.nombre}"  # Asegúrate de que Cliente tenga un campo nombre


class ItemCarrito(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE, related_name='items')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Item {self.id} - Carrito {self.carrito.id}"
