from django import forms

class ClienteForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    fecha_nacimiento = forms.DateField()

class BuscarClientesForm(forms.Form):
    criterio_nombre =forms.CharField(max_length=100)

class ArticuloForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    descripcion = forms.CharField(max_length=100)
    
class BuscarArticulosForm(forms.Form):
    criterio_nombre = forms.CharField(max_length=100)

class ProveedorForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    razon_social = forms.CharField(max_length=100)
    rubro = forms.CharField(max_length=100)

class BuscarProveedoresForm(forms.Form):
    criterio_rubro = forms.CharField(max_length=100)
