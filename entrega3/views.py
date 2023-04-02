from django.shortcuts import render
from entrega3.models import Cliente, Articulo, Proveedor
from entrega3.forms import ClienteForm, BuscarClientesForm, ArticuloForm, BuscarArticulosForm, ProveedorForm, BuscarProveedoresForm
from django.views.generic import ListView

def mostrar_clientes(request):

    clientes = Cliente.objects.all()
    total_clientes = len(clientes)
    context = {
        "clientes": clientes,
        "total_clientes": total_clientes,
        "form": ClienteForm(),
    }
    return render(request, "entrega3/clientes.html", context)


def crear_clientes(request):

    f = ClienteForm(request.POST)
    context = {
        "form": f
    }
    if f.is_valid():
        Cliente(nombre=f.data["nombre"], apellido=f.data["apellido"],  fecha_nacimiento=f.data
        ["fecha_nacimiento"]).save()
        context['form'] = ClienteForm()

    
    context["clientes"] = Cliente.objects.all()
    context["total_clientes"] = len(Cliente.objects.all())

    return render(request, "entrega3/clientes.html", context)


class BuscarClientes(ListView):
    model = Cliente
    context_object_name = "clientes"

    def get_queryset(self):
        f = BuscarClientesForm(self.request.GET)
        if f.is_valid():
           return Cliente.objects.filter(nombre__icontains=f.data["criterio_nombre"]).all()
        return Cliente.objects.none()



def mostrar_articulos(request):

    articulos = Articulo.objects.all()
    total_articulos = len(articulos)
    context = {
        "articulos": articulos,
        "total_articulos": total_articulos,
        "form": ArticuloForm(),
    }
    return render(request, "entrega3/articulos.html", context)


def crear_articulos(request):

    f = ArticuloForm(request.POST)
    context = {
        "form": f
    }
    if f.is_valid():
        Articulo(nombre=f.data["nombre"], descripcion=f.data["descripcion"]).save()
        context['form'] = ArticuloForm()

    
    context["articulos"] = Articulo.objects.all()
    context["total_articulos"] = len(Articulo.objects.all())

    return render(request, "entrega3/articulos.html", context)


class BuscarArticulos(ListView):
    model = Articulo
    context_object_name = "articulos"

    def get_queryset(self):
        f = BuscarArticulosForm(self.request.GET)
        if f.is_valid():
           return Articulo.objects.filter(nombre__icontains=f.data["criterio_nombre"]).all()
        return Articulo.objects.none()


def mostrar_proveedores(request):

    proveedores = Proveedor.objects.all()
    total_proveedores = len(proveedores)
    context = {
        "proveedores": proveedores,
        "total_proveedores": total_proveedores,
        "form": ProveedorForm(),
    }
    return render(request, "entrega3/proveedores.html", context)


def crear_proveedores(request):

    f = ProveedorForm(request.POST)
    context = {
        "form": f
    }
    if f.is_valid():
        Proveedor(nombre=f.data["nombre"], razon_social=f.data["razon_social"],  rubro=f.data
        ["rubro"]).save()
        context['form'] = ProveedorForm()

    
    context["proveedores"] = Proveedor.objects.all()
    context["total_proveedores"] = len(Proveedor.objects.all())

    return render(request, "entrega3/proveedores.html", context)


class BuscarProveedores(ListView):
    model = Proveedor
    context_object_name = "proveedores"

    def get_queryset(self):
        f = BuscarProveedoresForm(self.request.GET)
        if f.is_valid():
           return Proveedor.objects.filter(nombre__icontains=f.data["criterio_razon_social"]).all()
        return Proveedor.objects.none()