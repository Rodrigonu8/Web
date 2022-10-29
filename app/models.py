
from django.db import models

class Empresa(models.Model):
    id_empresa = models.BigIntegerField(primary_key=True)
    nombre_empresa = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'empresa'


AVANCE_CHOICES = (
    ('En Preparacion','En Preparacion'),
    ('En Desarrollo','En Desarrollo'),
    ('Finalizado','Finalizado'),
)
class FlujoDeTarea(models.Model):
    id_flujo = models.BigIntegerField(primary_key=True)
    nombre_flujo = models.CharField(max_length=500)
    avance = models.CharField(max_length=20,choices=AVANCE_CHOICES, default='En Preparacion')

    class Meta:
        managed = False
        db_table = 'flujo_de_tarea'

class Permiso(models.Model):
    id_permiso = models.BigIntegerField(primary_key=True)
    nombre_permiso = models.CharField(max_length=500)
    rol_id_rol = models.ForeignKey('Rol', models.DO_NOTHING, db_column='rol_id_rol')

    class Meta:
        managed = False
        db_table = 'permiso'

class Reporte(models.Model):
    id_problema = models.BigIntegerField(primary_key=True)
    comentario = models.CharField(max_length=500)
    plazo_solucion = models.DateField()

    class Meta:
        managed = False
        db_table = 'reporte'


class Rol(models.Model):
    id_rol = models.BigIntegerField(primary_key=True)
    nombre_rol = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'rol'


class Semaforo(models.Model):
    id_semaforo = models.BigIntegerField(primary_key=True)
    estado_semaforo = models.CharField(max_length=500)
    tarea_id_tarea = models.OneToOneField('Tarea', models.DO_NOTHING, db_column='tarea_id_tarea')

    class Meta:
        managed = False
        db_table = 'semaforo'

class Tarea(models.Model):
    id_tarea = models.BigIntegerField(primary_key=True)
    nombre_tarea = models.CharField(max_length=500)
    descripcion_tarea = models.CharField(max_length=500)
    fecha_inicio = models.DateField()
    fecha_termino = models.DateField()
    avance = models.CharField(max_length=20,choices=AVANCE_CHOICES, default='En Preparacion')
    usuario_id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='usuario_id_usuario')
    reporte_id_problema = models.ForeignKey(Reporte, models.DO_NOTHING, db_column='reporte_id_problema', blank=True, null=True)
    flujo_de_tarea_id_flujo = models.ForeignKey(FlujoDeTarea, models.DO_NOTHING, db_column='flujo_de_tarea_id_flujo', blank=True, null=True)
    tarea_sub_id_tarea_sub = models.BigIntegerField(unique=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tarea'

class TareaSub(models.Model):
    id_tarea_sub = models.BigIntegerField(primary_key=True)
    nombre_tarea_sub = models.CharField(max_length=500)
    descripcion_tarea_sub = models.CharField(max_length=500)
    fecha_inicio_sub = models.DateField()
    fecha_termino_sub = models.DateField()
    avance = models.CharField(max_length=20,choices=AVANCE_CHOICES, default='En Preparacion')
    tarea_id_tarea = models.BigIntegerField(unique=True, blank=True, null=True)
    usuario_id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='usuario_id_usuario')

    class Meta:
        managed = False
        db_table = 'tarea_sub'


class UnidadInterna(models.Model):
    id_unidad = models.BigIntegerField(primary_key=True)
    nombre_unidad = models.CharField(max_length=500)
    empresa_id_empresa = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='empresa_id_empresa')

    class Meta:
        managed = False
        db_table = 'unidad_interna'


class Usuario(models.Model):
    id_usuario = models.BigIntegerField(primary_key=True)
    nombre_usuario = models.CharField(max_length=500)
    contraseña_usuario = models.CharField(max_length=500)
    correo_usuario = models.CharField(max_length=500)
    empresa_id_empresa = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='empresa_id_empresa')
    rol_id_rol = models.ForeignKey(Rol, models.DO_NOTHING, db_column='rol_id_rol')
    unidad_interna_id_unidad = models.ForeignKey(UnidadInterna, models.DO_NOTHING, db_column='unidad_interna_id_unidad')

    class Meta:
        managed = False
        db_table = 'usuario'
