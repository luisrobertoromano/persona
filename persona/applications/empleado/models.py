from django.db import models
from applications.oficina.models import Oficina
from django.db.models.signals import post_delete

# Create your models here.
class Habilidad(models.Model):
    """Model definition for Habilidad."""

    nombre = models.CharField('Nombre de la habilidad', max_length=50)

    class Meta:
        """Meta definition for Habilidad."""

        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades'

    def __str__(self):
        """Unicode representation of Habilidad."""
        return self.nombre



class Empleado(models.Model):
    """Model definition for Empleado."""

    apellidos = models.CharField('Apellidos', max_length=50)
    nombres = models.CharField('Nombre', max_length=50)
    nombre_completo = models.CharField('Nombre Completo', max_length=50, blank=True)
    dni = models.CharField('DNI', max_length=50)
    area = models.ForeignKey(Oficina, on_delete=models.CASCADE)
    habilidades = models.ManyToManyField(Habilidad)
    avatar = models.ImageField('Imagen', upload_to='empleado', height_field=None, width_field=None, max_length=None, blank=True)


    class Meta:
        """Meta definition for Empleado."""

        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'

    def __str__(self):
        """Unicode representation of Empleado."""
        return self.apellidos + ", " + self.nombres


