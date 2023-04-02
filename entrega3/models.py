from django.db import models


class Cliente(models.Model):
    nombre = models.TextField(max_length=100)
    apellido = models.TextField(max_length=100)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return f"{self.id} - {self.nombre} - {self.apellido}"


class Articulo(models.Model):
    nombre = models.TextField(max_length=100)
    descripcion = models.TextField(max_length=100)
    
    
    def __str__(self):
        return f"{self.id} - {self.nombre} - {self.descripcion}"


class Proveedor(models.Model):
    nombre = models.TextField(max_length=100)
    razon_social = models.TextField(max_length=100)
    rubro = models.TextField(max_length=100)

    def __str__(self):
        return f"{self.id} - {self.nombre} - {self.razon_social} - {self.rubro}"
