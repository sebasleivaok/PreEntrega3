"""proyecto_entrega URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from entrega3.views import (mostrar_clientes, 
                            crear_clientes, 
                            BuscarClientes, 
                            mostrar_articulos, 
                            crear_articulos, 
                            BuscarArticulos, 
                            mostrar_proveedores, 
                            crear_proveedores, 
                            BuscarProveedores)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clientes/', mostrar_clientes, name="clientes"),
    path('clientes/create/', crear_clientes, name="clientes-create"),
    path('clientes/list/', BuscarClientes.as_view(), name="clientes-list"),
    path('articulos/', mostrar_articulos, name="articulos"),
    path('articulos/create/', crear_articulos, name="articulos-create"),
    path('articulos/list/', BuscarArticulos.as_view(), name="articulos-list"),
    path('proveedores/', mostrar_proveedores, name="proveedores"),
    path('proveedores/create/', crear_proveedores, name="proveedores-create"),
    path('proveedores/list/', BuscarProveedores.as_view(), name="proveedores-list"),
]
