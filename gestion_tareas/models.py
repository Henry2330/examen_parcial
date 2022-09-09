from django.db import models

# Create your models here.
class tarea(models.Model):
    descripcion = models.CharField(max_length=128,default='')
    fechas_de_creacion = models.CharField(max_length=128,default='')
    fecha_de_entrega = models.CharField(max_length=128,default='')
    usuario_responsable = models.CharField(max_length=128,default='')
    estado_de_tarea = models.CharField(max_length=128,default='')

class usuario(models.Model):
    nombre = models.CharField(max_length=128,default='')
    apellido = models.CharField(max_length=128,default='')
    codigo_de_usuario = models.CharField(max_length=128,default='')
    contraseña = models.CharField(max_length=128,default='')