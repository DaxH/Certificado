from django.db import models

# Create your models here.

class Usuario(models.Model):
    """Usuario description)"""

    cedula = models.CharField(blank=True, max_length=10)
    nombre = models.CharField(blank=True, max_length=100)
    apellido = models.CharField(blank=True, max_length=100)

    def __str__(self):
        return self.nombre
