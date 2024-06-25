from django.urls import path
from . import views

urlpatterns = [
    path('registro_ventas/', views.registro_ventas, name='registro_ventas'),
    path('detalle_venta/<int:venta_id>/', views.detalle_venta, name='detalle_venta'),
    path('carrito/<int:cliente_id>/', views.carrito, name='carrito'),  # Añadir esta ruta
]
