from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.db import transaction
from .models import Venta, Detalle, Carrito, ItemCarrito, Producto
from .forms import VentaForm, DetalleVentaForm, ItemCarritoForm
from clientes.models import Cliente

def obtener_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    data = {
        'precio_unitario': producto.precio,
        'stock_disponible': producto.stock
    }
    return JsonResponse(data)

def eliminar_producto_carrito(request, producto_id):
    if request.method == 'POST':
        carrito_item = get_object_or_404(Carrito, producto_id=producto_id, usuario=request.user)
        carrito_item.delete()
        return redirect('ver_carrito')

def ver_carrito(request, cliente_id):
    carrito, created = Carrito.objects.get_or_create(cliente_id=cliente_id)
    items = ItemCarrito.objects.filter(carrito=carrito)

    return render(request, 'ver_carrito.html', {
        'carrito': carrito,
        'items': items,
    })

def agregar_producto_carrito(request, carrito_id):
    carrito = get_object_or_404(Carrito, id=carrito_id)

    if request.method == 'POST':
        item_form = ItemCarritoForm(request.POST)
        if item_form.is_valid():
            item = item_form.save(commit=False)
            item.carrito = carrito
            item.precio_unitario = item.producto.precio
            item.subtotal = item.cantidad * item.precio_unitario
            item.save()
            return redirect('ver_carrito', cliente_id=carrito.cliente.id)
    else:
        item_form = ItemCarritoForm()

    return render(request, 'agregar_producto_carrito.html', {
        'carrito': carrito,
        'item_form': item_form,
    })

@transaction.atomic
def confirmar_venta(request):
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
    })
