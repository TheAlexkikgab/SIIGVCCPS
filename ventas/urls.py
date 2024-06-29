from django.urls import path
from . import views

urlpatterns = [
    path('carrito/<int:cliente_id>/', views.ver_carrito, name='ver_carrito'),
    path('confirmar_venta/<int:cliente_id>/', views.confirmar_venta, name='confirmar_venta'),
    path('obtener-producto/<int:producto_id>/', views.obtener_producto, name='obtener_producto'),
    path('agregar_producto_carrito/<int:carrito_id>/', views.agregar_producto_carrito, name='agregar_producto_carrito'),
    path('carrito/eliminar/<int:item_id>/', views.eliminar_producto_carrito, name='eliminar_producto_carrito'),
    path('carrito/eliminar_todo/<int:carrito_id>/', views.eliminar_carrito, name='eliminar_carrito'),
]
