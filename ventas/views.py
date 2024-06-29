from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.db import transaction
from django.db.models import Sum
from django.contrib import messages
from .models import Venta, Detalle, Carrito, ItemCarrito, Producto
from .forms import VentaForm, DetalleVentaForm, ItemCarritoForm
from clientes.models import Cliente
from decimal import Decimal

def obtener_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    data = {
        'precio_unitario': producto.precio,
        'stock_disponible': producto.stock
    }
    return JsonResponse(data)

def eliminar_producto_carrito(request, item_id):
    item = get_object_or_404(ItemCarrito, id=item_id)
    carrito_id = item.carrito.id
    item.delete()
    return redirect('ver_carrito', cliente_id=item.carrito.cliente.id)

def ver_carrito(request, cliente_id):
    carrito, created = Carrito.objects.get_or_create(cliente_id=cliente_id)
    items = ItemCarrito.objects.filter(carrito=carrito)
    total = items.aggregate(total=Sum('subtotal'))['total'] or 0
    

    return render(request, 'ver_carrito.html', {
        'carrito': carrito,
        'items': items,
        'total': total,
    })

def agregar_producto_carrito(request, carrito_id):
    carrito = get_object_or_404(Carrito, id=carrito_id)

    if request.method == 'POST':
        item_form = ItemCarritoForm(request.POST)
        if item_form.is_valid():
            item = item_form.save(commit=False)
            item.carrito = carrito
            item.precio_unitario = item.producto.precio
            
            # Verificar si el producto ya está en el carrito
            existing_item = ItemCarrito.objects.filter(carrito=carrito, producto=item.producto).first()
            if existing_item:
                existing_item.cantidad += item.cantidad
                existing_item.subtotal = existing_item.cantidad * existing_item.precio_unitario
                existing_item.save()
            else:
                item.subtotal = item.cantidad * item.precio_unitario
                item.save()

            return redirect('ver_carrito', cliente_id=carrito.cliente.id)
    else:
        item_form = ItemCarritoForm()

    return render(request, 'agregar_producto_carrito.html', {
        'carrito': carrito,
        'item_form': item_form,
    })

from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Carrito, ItemCarrito, Producto

def eliminar_carrito(request, carrito_id):
    carrito = get_object_or_404(Carrito, id=carrito_id)
    carrito.delete()
    return redirect('ver_carrito', cliente_id=carrito.cliente.id)


@transaction.atomic
def confirmar_venta(request, cliente_id):
    # Obtener el carrito asociado con el cliente
    carrito = get_object_or_404(Carrito, cliente_id=cliente_id)
    items = ItemCarrito.objects.filter(carrito=carrito)

    if not items.exists():
        # Si el carrito está vacío, agregar un mensaje de error
        messages.error(request, 'El carrito está vacío')
        return redirect('ver_carrito', cliente_id=cliente_id)

    # Calcular el subtotal
    subtotal = sum(item.subtotal for item in items)
    subtotal = Decimal(subtotal)

    # Aplicar descuento y calcular el total después del descuento
    descuento = Decimal(0)
    impuesto = Decimal(0)

    if request.method == 'POST':
        venta_form = VentaForm(request.POST)
        if venta_form.is_valid():
            venta = venta_form.save(commit=False)
            venta.cliente = carrito.cliente

            descuento = Decimal(request.POST.get('descuento', 0))
            impuesto = Decimal(request.POST.get('impuesto', 0))

            total_con_descuento = subtotal - (subtotal * (descuento / Decimal(100)))
            total_final = total_con_descuento + (total_con_descuento * (impuesto / Decimal(100)))

            venta.total = total_final
            venta.descuento = descuento
            venta.impuestos = impuesto
            venta.estatus_venta = 'Pendiente'
            venta.save()

            # Crear los detalles de la venta
            for item in items:
                Detalle.objects.create(
                    id_venta=venta,
                    id_producto=item.producto,
                    cantidad=item.cantidad,
                    precio_unitario=item.precio_unitario,
                    subtotal=item.subtotal
                )
                # Disminuir el stock del producto
                producto = item.producto
                producto.stock -= item.cantidad
                producto.save()

            carrito.delete()  # Elimina el carrito después de la venta

            # Renderizar la página de confirmación de venta con los detalles
            return render(request, 'venta_confirmada.html', {
                'venta': venta,
                'items': items,
                'total': total_final,
                'carrito': carrito,
            })
    else:
        venta_form = VentaForm()

        total_con_descuento = subtotal - (subtotal * (descuento / Decimal(100)))
        total_final = total_con_descuento + (total_con_descuento * (impuesto / Decimal(100)))

    return render(request, 'confirmar_venta.html', {
        'venta_form': venta_form,
        'items': items,
        'total': total_final,
    })
