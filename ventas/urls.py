from django.urls import path
from . import views

urlpatterns = [
    path('carrito/<int:cliente_id>/', views.ver_carrito, name='ver_carrito'),
    path('confirmar_venta/', views.confirmar_venta, name='confirmar_venta'),
    path('obtener-producto/<int:producto_id>/', views.obtener_producto, name='obtener_producto'),
]
