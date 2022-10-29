from email import message
from inspect import formatargvalues
from msilib.schema import CreateFolder
from re import template
from django.shortcuts import render
from .models import *
from django.urls import reverse, reverse_lazy
from django.views.generic import UpdateView
from .forms import CrearFlujo, CrearPermisos, CrearROL, CrearTareaSUB, CrearUni, CrearTarea, CrearUsuario, ModTarea, CrearProblema, ModTareaSub, ModFlujo
# Create your views here.
from django.shortcuts import redirect
from datetime import date, timedelta

def home(request):
    return render(request, 'Base.html')

# Creación de Objetos


def CrearUser(request):
    data = {
        'form': CrearUsuario()
    }
    if request.method == 'POST':
        formulario = CrearUsuario(data=request.POST)
        if formulario.is_valid():
            formulario.save()

    return render(request, 'Administrador/crear_usuario.html', data)


def CrearTask(request):
    data = {
        'form': CrearTarea()
    }
    if request.method == 'POST':
        formulario = CrearTarea(data=request.POST)
        if formulario.is_valid():
            formulario.save()
    return render(request, 'Funcionario/crear_tarea.html', data)


def CrearUniInt(request):
    data = {
        'form': CrearUni()
    }
    if request.method == 'POST':
        formulario = CrearUni(data=request.POST)
        if formulario.is_valid():
            formulario.save()
    return render(request, 'Administrador/crear_uni.html', data)


def CrearRol(request):
    data = {
        'form': CrearROL()
    }
    if request.method == 'POST':
        formulario = CrearROL(data=request.POST)
        if formulario.is_valid():
            formulario.save()
    return render(request, 'Administrador/crear_rol.html', data)


def CrearFlujoTarea(request):
    data = {
        'form': CrearFlujo()
    }
    if request.method == 'POST':
        formulario = CrearFlujo(data=request.POST)
        if formulario.is_valid():
            formulario.save()
    return render(request, 'Administrador/crear_flujo.html', data)


def CrearTareaSub(request):
    data = {
        'form': CrearTareaSUB()
    }
    if request.method == 'POST':
        formulario = CrearTareaSUB(data=request.POST)
        if formulario.is_valid():
            formulario.save()
    return render(request, 'Funcionario/crear_tareasub.html', data)


def CrearPermiso(request):
    data = {
        'form': CrearPermisos()
    }
    if request.method == 'POST':
        formulario = CrearPermisos(data=request.POST)
        if formulario.is_valid():
            formulario.save()
    return render(request, 'Administrador/crear_permisos.html', data)

def CrearProblem(request):
    data = {
        'form': CrearProblema()
    }
    if request.method == 'POST':
        formulario = CrearProblema(data=request.POST)
        if formulario.is_valid():
            formulario.save()
    return render(request, 'Funcionario/problema.html', data)

# Listados


def listar_tareas(request):
    tareas = Tarea.objects.all()
    return render(request, "Funcionario/listar_tareas.html", {'tareas': tareas})


def listar_tareassub(request):
    tareassub = TareaSub.objects.all()
    return render(request, "Funcionario/listar_tareassub.html", {'tareassub': tareassub})


def listar_empresas(request):
    empresas = Empresa.objects.all()
    return render(request, "Administrador/listar_empresas.html", {'empresas': empresas})


def listar_uni(request):
    uniint = UnidadInterna.objects.all()
    return render(request, "Administrador/listar_uni.html", {'uniint': uniint})


def listar_rol(request):
    roles = Rol.objects.all()
    return render(request, "Administrador/listar_rol.html", {'roles': roles})


def listar_usu(request):
    user = Usuario.objects.all()
    return render(request, "Administrador/listar_usuario.html", {'user': user})


def listar_flujo(request):
    flujo = FlujoDeTarea.objects.all()
    return render(request, "Administrador/listar_flujo.html", {'flujo': flujo})


def listar_permisos(request):
    permi = Permiso.objects.all()
    return render(request, "Administrador/listar_permisos.html", {'permi': permi})


def listar_problemas(request):
    reporte = Reporte.objects.all()
    return render(request, "Funcionario/listar_reporte.html", {'reporte': reporte})



def editar_Tarea(request, id_tarea):
    instancia = Tarea.objects.get(id_tarea=id_tarea)
    form = ModTarea(instance=instancia)
    if request.method == "POST":
        form = ModTarea(request.POST, instance=instancia)
    if form.is_valid():
        instancia = form.save(commit=False)
        instancia.save()
    return render(request, "Funcionario/editar_tarea.html", {'form': form})

def editar_Tareasub(request, id_tarea_sub):
    instancia = TareaSub.objects.get(id_tarea_sub=id_tarea_sub)
    form = ModTareaSub(instance=instancia)
    if request.method == "POST":
        form = ModTareaSub(request.POST, instance=instancia)
    if form.is_valid():
        instancia = form.save(commit=False)
        instancia.save()
    return render(request, "Funcionario/editar_tareasub.html", {'form': form})


def editar_flujo(request, id_flujo):
    instancia = FlujoDeTarea.objects.get(id_flujo=id_flujo)
    form = ModFlujo(instance=instancia)
    if request.method == "POST":
        form = ModFlujo(request.POST, instance=instancia)
    if form.is_valid():
        instancia = form.save(commit=False)
        instancia.save()
    return render(request, "Funcionario/editar_flujo.html", {'form': form})

def abrir_tarea(request, id_tarea):
    tarea = Tarea.objects.get(id_tarea=id_tarea)
    today = date.today()
    fecha_actual = today.strftime("%Y-%m-%d")
    fecha_final = str(tarea.fecha_termino)
    fecha_7diasantes = tarea.fecha_termino - timedelta(weeks=1)
    fecha_amarilla = str(fecha_7diasantes)

    print(fecha_final)
    print(fecha_actual)
    print(fecha_amarilla)
    return render(request, "Funcionario/tarea.html", {'tarea': tarea, 'fecha_actual': fecha_actual, 'fecha_final':fecha_final, 'fecha_amarilla':fecha_amarilla})

def abrir_tareasub(request, id_tarea_sub):
    tarea = TareaSub.objects.get(id_tarea_sub=id_tarea_sub)
    return render(request, "Funcionario/tareasub.html", {'tarea': tarea})

def mostrar_empleados(request):
    usuarios = Usuario.objects.all()
    return render(request, "Funcionario/listar_empleados.html", {'usuarios': usuarios})

def tareas_usuarios(request, usuario_id_usuario):
    tareas = Tarea.objects.get(usuario_id_usuario=usuario_id_usuario)
    return render(request, "Funcionario/tareas_usuarios.html",{'tareas':tareas})

def listar_unidad_resumen(request):
    uni = Usuario.objects.all()
    return render(request, "Administrador/listar_unidades_resumen.html", {'uni': uni})






