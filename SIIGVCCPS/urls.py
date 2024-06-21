"""
URL configuration for SIIGVCCPS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from productos import views as productos_views
from clientes import views as clientes_views
from ventas import views as ventas_views
from home import views as home_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('productos/', productos_views.mostrar_html),
    path('', home_views.home, name='home'),
    path('login/', home_views.login, name='login'),
    #path('clientes/', clientes_views.),
    #path('ventas/', ventas_views.),
]