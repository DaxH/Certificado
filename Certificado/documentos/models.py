from django.db import models
from usuarios.models import Usuario
from carreras.models import Carrera

class Entidad(models.Model):
    """(Entidad description)"""

    TIPO = (
    ('1','Entidad Receptora'),
    ('2','Entidad Emisora'),
    )
    institucion = models.CharField(blank=True, max_length=100)
    representante = models.CharField(blank=True, max_length=100)
    logo = models.ImageField(upload_to="static/imagenes")
    tipo = models.CharField(choices=TIPO, max_length=1)

    def __str__(self):
        return self.institucion


class Documento(models.Model):
    """(Documento description)"""
    nombre = models.CharField(blank=True, max_length=150)
    codigo = models.CharField(blank=False, max_length=25)
    fecha = models.DateField(blank=False)
    duracion = models.IntegerField(blank=False, null=False)
    usuario = models.ManyToManyField(Usuario, null=True )
    carrera = models.ForeignKey(Carrera, null=False, on_delete=models.CASCADE)
    entidad = models.ManyToManyField(Entidad, null=True)

    def __str__(self):
        return self.nombre
