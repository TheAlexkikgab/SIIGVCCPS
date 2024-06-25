from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente
from .forms import ClienteForm, CedulaForm
from ventas.models import Venta  

def verificar_cedula(request):
    if request.method == 'POST':
        form = CedulaForm(request.POST)
        if form.is_valid():
            cedula = form.cleaned_data['cedula']
            try:
                cliente = Cliente.objects.get(cedula=cedula)
                # Redirigir al carrito (debes ajustar esta URL según tus URLs)
                return redirect('carrito', cliente_id=cliente.id)
            except Cliente.DoesNotExist:
                return redirect('registrar_cliente', cedula=cedula)
    else:
        form = CedulaForm()
    return render(request, 'clientes/verificar_cedula.html', {'form': form})

def registrar_cliente(request, cedula=None):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('carrito', cliente_id=form.instance.id)
    else:
        form = ClienteForm(initial={'cedula': cedula})
    return render(request, 'clientes/registrar_cliente.html', {'form': form})

def gestion_clientes(request):
    clientes = Cliente.objects.all()
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gestion_clientes')
    else:
        form = ClienteForm()
    return render(request, 'clientes/gestion_clientes.html', {'clientes': clientes, 'form': form})
