from django.db import models
from usuarios.models import Usuario
from carreras.models import Carrera

class EntidadEmisora(models.Model):
    """(Entidad description)"""

    institucion = models.CharField(blank=True, max_length=100)
    representante = models.CharField(blank=True, max_length=100)
    logo = models.ImageField(upload_to="static/imagenes")

    def __str__(self):
        return self.institucion

class Documento(models.Model):
    """(Documento description)"""
    nombre = models.CharField(blank=False, max_length=150)
    codigo = models.CharField(blank=False, max_length=25, unique=True)
    fecha_inicio = models.DateField(blank=False, null=True)
    hora = models.TimeField(null = True, blank=False)
    fecha_fin = models.DateField(null = True, blank=False)
    duracion = models.IntegerField(blank=False, null=False)
    usuario = models.ManyToManyField(Usuario, null=True, blank=True)
    barrio = models.CharField(null=True, blank=True, max_length=30)
    parroquia = models.CharField(null=True, blank=True, max_length=30)
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE, null=True, blank=True)
    entidad_emisora = models.ManyToManyField(EntidadEmisora, null=True, blank=True)

    def __str__(self):
        return self.nombre
