from django import forms
from .models import Clientes

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = ['cedula', 'pasaporte', 'nombres', 'apellidos', 'nacimiento', 'direccion', 'telefono', 'email']