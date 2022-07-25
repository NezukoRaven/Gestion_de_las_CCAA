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

class FormPago(models.Model):
    carrera = models.CharField(max_length=100, null=True, blank=True, verbose_name='Carrera')
    sede = models.CharField(max_length=100, null=True, blank=True, verbose_name='Sede')
    nivel = models.IntegerField(null=True, blank=True, verbose_name='Celular colaborador')
    periodo = models.CharField(max_length=100, null=True, blank=True, verbose_name='Periodo')
    año = models.CharField(max_length=100,null=True, blank=True, verbose_name='Año')
    reunion_1 = models.CharField(max_length=100,null=True, blank=True, verbose_name='Fecha Reunión 1')
    reunion_1_link = models.CharField(max_length=100,null=True, blank=True, verbose_name='Link 1')
    reunion_2 = models.CharField(max_length=100,null=True, blank=True, verbose_name='Fecha Reunión 2')
    reunion_2_link = models.CharField(max_length=100,null=True, blank=True, verbose_name='Link 2')
    reunion_3 = models.CharField(max_length=100,null=True, blank=True, verbose_name='Fecha Reunión 3')
    reunion_3_link = models.CharField(max_length=100,null=True, blank=True, verbose_name='Link 3')
    class Meta:
        verbose_name = 'Formulario de Pago'
        verbose_name_plural = 'Formularios de Pago'
        ordering = ['carrera']
    def _str_(self):
        return self.carrera

class Informe(models.Model):
    metodologias = models.CharField(max_length=150, null=True, blank=True, verbose_name='Metodologias')
    capacitaciones = models.CharField(max_length=150, null=True, blank=True, verbose_name='Capacitaciones')
    actividades = models.CharField(max_length=150, null=True, blank=True, verbose_name='Actividades')
    otros = models.CharField(max_length=150, null=True, blank=True, verbose_name='Otros')
    objetivo = models.TextField(verbose_name='Objetivo')
    estrategia = models.TextField(verbose_name='Estrategia')
    respuesta2 = models.TextField(verbose_name='Respuesta2')
    respuesta3 = models.TextField(verbose_name='Respuesta3')
    respuesta4 = models.TextField(verbose_name='Respuesta4')

    class Meta:
        verbose_name = 'Informe'
        verbose_name_plural = 'Informes'
        ordering = ['metodologias']
    def _str_(self):
        return self.metodologias

class Ver_informe(models.Model):
    verinforme = models.IntegerField(null=True, blank=True, verbose_name='informe_id')
    periodo = models.CharField(max_length=100, null=True, blank=True, verbose_name='Periodo')
    sede = models.CharField(max_length=100, null=True, blank=True, verbose_name='Sede')
    carrera = models.CharField(max_length=100, null=True, blank=True, verbose_name='Carrera')
    nivel = models.IntegerField(null=True, blank=True, verbose_name='Nivel')

    class Meta:
        verbose_name = 'VerInforme'
        verbose_name_plural = 'VerInformes'
        ordering = ['periodo']
    def _str_(self):
        return self.periodo
