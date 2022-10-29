from django.contrib import admin
from .models import Empresa, Reporte, FlujoDeTarea, Permiso, Rol, Semaforo, Tarea, TareaSub, UnidadInterna, Usuario



admin.site.register(Usuario)
admin.site.register(Empresa)
admin.site.register(Reporte)
admin.site.register(FlujoDeTarea)
admin.site.register(Rol)
admin.site.register(Semaforo)
admin.site.register(Tarea)
admin.site.register(TareaSub)
admin.site.register(UnidadInterna)
admin.site.register(Permiso)


