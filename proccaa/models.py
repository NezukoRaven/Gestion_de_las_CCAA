from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=100, null=True, blank=True, verbose_name='Nombre colaborador')
    correo = models.CharField(max_length=100, null=True, blank=True, verbose_name='Correo colaborador')
    rut = models.CharField(max_length=100, null=True, blank=True, verbose_name='Rut colaborador')
    cargo = models.CharField(max_length=100, null=True, blank=True, verbose_name='Cargo colaborador')
    celular = models.IntegerField(null=True, blank=True, verbose_name='Celular colaborador')
    estado= models.CharField(max_length=10,null=True, blank=True, verbose_name='Estado colaborador', default='Activo')

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['nombre']
    def _str_(self):
        return self.nombre