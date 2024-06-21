from django import forms
from .models import Productos

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = ['nombre', 'descripcion', 'precio', 'categoria', 'marca', 'elaboracion', 'caducidad', 'stock']
