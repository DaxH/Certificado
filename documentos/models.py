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
    nombre = models.CharField(blank=True, max_length=150)
    codigo = models.CharField(blank=False, max_length=25, unique=True)
    fecha = models.DateField(blank=False)
    duracion = models.IntegerField(blank=False, null=False)
    usuario = models.ManyToManyField(Usuario, null=True )
    carrera = models.ForeignKey(Carrera, null=False, on_delete=models.CASCADE)
    entidad_emisora = models.ManyToManyField(EntidadEmisora, null=True)

    def __str__(self):
        return self.nombre
