from dataclasses import field, fields
from pyexpat import model
from socket import fromshare
from tkinter import Widget
from django import forms
from .models import FlujoDeTarea, Permiso, Rol, Tarea, TareaSub, UnidadInterna, Usuario, Reporte


class CrearUsuario(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'

class CrearTarea(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ('id_tarea','nombre_tarea','descripcion_tarea','fecha_inicio','fecha_termino','usuario_id_usuario','flujo_de_tarea_id_flujo')


class CrearUni(forms.ModelForm):
    class Meta:
        model = UnidadInterna
        fields = '__all__'


class CrearROL(forms.ModelForm):
    class Meta:
        model = Rol
        fields = '__all__'


class CrearFlujo(forms.ModelForm):
    class Meta:
        model = FlujoDeTarea
        fields = ('id_flujo','nombre_flujo')


class CrearTareaSUB(forms.ModelForm):
    class Meta:
        model = TareaSub
        fields = ('id_tarea_sub','nombre_tarea_sub','descripcion_tarea_sub','fecha_inicio_sub','fecha_termino_sub','usuario_id_usuario','tarea_id_tarea' )

class CrearPermisos(forms.ModelForm):
    class Meta:
        model = Permiso
        fields = '__all__'

class ModTarea(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = '__all__'

class ModTareaSub(forms.ModelForm):
    class Meta:
        model = TareaSub
        fields = '__all__'

class CrearProblema(forms.ModelForm):
    class Meta:
        model = Reporte
        fields = '__all__'

class ModFlujo(forms.ModelForm):
    class Meta:
        model = FlujoDeTarea
        fields = ('id_flujo','avance')