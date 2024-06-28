from django.shortcuts import render, redirect, get_object_or_404
from .models import Venta, Detalle, Carrito, ItemCarrito, Producto
from .forms import VentaForm, DetalleVentaForm, ItemCarritoForm
from django.http import JsonResponse
from django.db import transaction
from clientes.models import Cliente

def obtener_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    data = {
        'precio_unitario': producto.precio,
        'stock_disponible': producto.stock
    }
    return JsonResponse(data)

def ver_carrito(request, cliente_id):
    carrito, created = Carrito.objects.get_or_create(cliente_id=cliente_id)
    items = ItemCarrito.objects.filter(carrito=carrito)
    productos = Producto.objects.all()

    if request.method == 'POST':
        item_form = ItemCarritoForm(request.POST)
        if item_form.is_valid():
            item = item_form.save(commit=False)
            item.carrito = carrito
            item.precio_unitario = item.producto.precio_unitario  # Asignar el precio unitario desde el producto
            item.subtotal = item.cantidad * item.precio_unitario
            item.save()
            return redirect('ver_carrito', cliente_id=cliente_id)
    else:
        item_form = ItemCarritoForm()

    return render(request, 'ver_carrito.html', {
        'carrito': carrito,
        'items': items,
        'item_form': item_form,
        'productos': productos,
    })

@transaction.atomic
def confirmar_venta(request):
    # Asumir que el cliente está autenticado y tiene un carrito
    cliente = request.user.cliente
    carrito = get_object_or_404(Carrito, cliente=cliente)
    items = ItemCarrito.objects.filter(carrito=carrito)

    if request.method == 'POST':
        venta_form = VentaForm(request.POST)
        if venta_form.is_valid():
            venta = venta_form.save(commit=False)
            venta.cliente = carrito.cliente
            venta.total = sum(item.subtotal for item in items)
            venta.save()

            for item in items:
                Detalle.objects.create(
                    id_venta=venta,
                    id_producto=item.producto,
                    cantidad=item.cantidad,
                    precio_unitario=item.precio_unitario,
                    subtotal=item.subtotal
                )
            carrito.delete()
            return redirect('lista_ventas')
    else:
        venta_form = VentaForm()

    return render(request, 'confirmar_venta.html', {
        'venta_form': venta_form,
        'items': items,
        'carrito': carrito
    })