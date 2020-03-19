from django.db import models

# Create your models here.

class Usuario(models.Model):
    """Usuario description)"""

    cedula = models.CharField(blank=False, max_length=10, unique=True)
    nombre = models.CharField(blank=False, max_length=100)
    apellido = models.CharField(blank=False, max_length=100)
    telefono = models.CharField(blank=True, max_length=10)

    def __str__(self):
        return '%s %s %s' % (self.nombre, self.apellido, self.cedula)
