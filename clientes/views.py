from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente
from .forms import ClienteForm, CedulaForm

def verificar_cedula(request):
    if request.method == 'POST':
        form = CedulaForm(request.POST)
        if form.is_valid():
            cedula = form.cleaned_data['cedula']
            try:
                cliente = Cliente.objects.get(cedula=cedula)
                return redirect('ver_carrito', cliente_id=cliente.id)
            except Cliente.DoesNotExist:
                return render(request, 'home.html', {'form': form, 'error_message': 'Cédula de Cliente no encontrada, por favor regístrese.'})
    else:
        form = CedulaForm()
    return render(request, 'home.html', {'form': form})


def registrar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ver_carrito', cliente_id=form.instance.id)
    else:
        form = ClienteForm()
    return render(request, 'registrar_cliente.html', {'form': form})

def gestion_clientes(request):
    clientes = Cliente.objects.all()
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gestion_clientes')
    else:
        form = ClienteForm()
    return render(request, 'gestion_clientes.html', {'clientes': clientes, 'form': form})
