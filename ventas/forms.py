from django import forms
from .models import Venta, Detalle

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['id_cliente', 'metodo_pago', 'estatus_venta', 'descuento', 'impuestos']

class DetalleVentaForm(forms.ModelForm):
    class Meta:
        model = Detalle
        fields = ['id_producto', 'cantidad', 'precio_unitario']