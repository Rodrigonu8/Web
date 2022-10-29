from django.urls import path, include
from django.shortcuts import render
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('CrearUsuario', views.CrearUser, name="crear_usuario"),
    path('CrearTarea', views.CrearTask, name="crear_tarea"),
    path('CrearUniInt', views.CrearUniInt, name="crear_uni"),
    path('CrearRol', views.CrearRol, name="crear_rol"),
    path('CrearFlujo', views.CrearFlujoTarea, name="crear_flujo"),
    path('CrearTareaSub', views.CrearTareaSub, name="crear_tareasub"),
    path('CrearProblema', views.CrearProblem, name="crear_problema"),
    path('listarProblemas', views.listar_problemas, name="listar_problemas"),
    path('listarTareas', views.listar_tareas, name="listar_tareas"),
    path('listarTareasSub', views.listar_tareassub, name="listar_tareassub"),
    path('listarEmpresas', views.listar_empresas, name="listar_empresas"),
    path('listarUni', views.listar_uni, name="listar_uni"),
    path('listarUsuario', views.listar_usu, name="listar_usuario"),
    path('listarRol', views.listar_rol, name="listar_rol"),
    path('listarFlujo', views.listar_flujo, name="listar_flujo"),
    path('crearPermiso', views.CrearPermiso, name="crear_permiso"),
    path('listarPermisos', views.listar_permisos, name="listar_permisos"),
    path('editar_tarea/<int:id_tarea>', views.editar_Tarea , name="mod_tarea"),
    path('editar_tareasub/<int:id_tarea_sub>', views.editar_Tareasub , name="mod_tareasub"),
    path('Tarea/<int:id_tarea>', views.abrir_tarea, name="abrir_tareas"),
    path('TareaSub/<int:id_tarea_sub>', views.abrir_tareasub, name="abrir_tareassub"),
    path('listarEmpleados', views.mostrar_empleados, name="listar_emp"),
    path('Carga/<int:usuario_id_usuario>', views.tareas_usuarios, name="tareas_usuarios"),
    path('Informes/', views.listar_unidad_resumen, name="listar_uni_resumen"),
    path('editar_flujo/<int:id_flujo>', views.editar_flujo , name="mod_flujo"),
]