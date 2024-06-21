from django import forms
from .models import Ventas, Detalles

class VentaForm(forms.ModelForm):
    class Meta:
        model = Ventas
        fields = ['id_cliente', 'metodo_pago', 'estatus_venta', 'descuento', 'impuestos']

class DetalleVentaForm(forms.ModelForm):
    class Meta:
        model = Detalles
        fields = ['id_producto', 'cantidad', 'precio_unitario']