from django.shortcuts import render, redirect
from .models import Venta, Detalle
from .forms import VentaForm, DetalleVentaForm

# Create your views here.

def registro_ventas(request):
    ventas = Venta.objects.all()
    if request.method == "POST":
        form = VentaForm(request.POST)
        if form.is_valid():
            venta = form.save()
            return redirect('detalle_venta', venta_id=venta.id)
    else:
        form = VentaForm()
    return render(request, 'ventas/registro_ventas.html', {'ventas': ventas, 'form': form})

def detalle_venta(request, venta_id):
    venta = Venta.objects.get(id=venta_id)
    detalles = Detalle.objects.filter(id_venta=venta)
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


