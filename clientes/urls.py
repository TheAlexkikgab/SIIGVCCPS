from django.urls import path
from . import views

urlpatterns = [
    path('verificar_cedula/', views.verificar_cedula, name='verificar_cedula'),
    path('registrar_cliente/<str:cedula>/', views.registrar_cliente, name='registrar_cliente'),
    path('gestion_clientes/', views.gestion_clientes, name='gestion_clientes'),
]
