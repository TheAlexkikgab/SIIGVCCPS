from django.shortcuts import render, redirect
from .models import Ventas, Detalles
from .forms import VentaForm, DetalleVentaForm

def registro_ventas(request):
    ventas = Ventas.objects.all()
    if request.method == "POST":
        form = VentaForm(request.POST)
        if form.is_valid():
            venta = form.save()
            return redirect('detalle_venta', venta_id=venta.id)
    else:
        form = VentaForm()
    return render(request, 'ventas/registro_ventas.html', {'ventas': ventas, 'form': form})

def detalle_venta(request, venta_id):
    venta = Ventas.objects.get(id=venta_id)
    detalles = Detalles.objects.filter(id_venta=venta)
    if request.method == "POST":
        form = DetalleVentaForm(request.POST)
        if form.is_valid():
            detalle = form.save(commit=False)
            detalle.id_venta = venta
            detalle.subtotal = detalle.cantidad * detalle.precio_unitario
            detalle.save()
            venta.total += detalle.subtotal
            venta.save()
            return redirect('detalle_venta', venta_id=venta.id)
    else:
        form = DetalleVentaForm()
    return render(request, 'ventas/detalle_venta.html', {'venta': venta, 'detalles': detalles, 'form': form})

# Create your views here.
