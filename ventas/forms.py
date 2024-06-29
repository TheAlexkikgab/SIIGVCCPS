from django import forms
from .models import Venta, Detalle, ItemCarrito, Producto

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['metodo_pago', 'estatus_venta', 'descuento', 'impuestos']
        widgets = {
            'metodo_pago': forms.TextInput(attrs={'class': 'form-control'}),
            'estatus_venta': forms.TextInput(attrs={'class': 'form-control'}),
            'descuento': forms.NumberInput(attrs={'class': 'form-control'}),
            'impuestos': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class DetalleVentaForm(forms.ModelForm):
    class Meta:
        model = Detalle
        fields = ['id_producto', 'cantidad', 'precio_unitario']
        widgets = {
            'id_producto': forms.Select(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
            'precio_unitario': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class ItemCarritoForm(forms.ModelForm):
    class Meta:
        model = ItemCarrito
        fields = ['producto', 'cantidad']
        widgets = {
            'producto': forms.Select(attrs={'class': 'form-control', 'id': 'id_producto'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control', 'id': 'id_cantidad'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['producto'].queryset = Producto.objects.all()  # Asegúrate de que aquí estás obteniendo los productos correctos
