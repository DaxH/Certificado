from django.db import models

# Create your models here.
class Carrera(models.Model):
    """(Carrera description)"""

    nombre = models.CharField(blank=True, max_length=30)

    def __str__(self):
        return self.nombre
