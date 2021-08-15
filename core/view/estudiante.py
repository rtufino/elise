from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from core.models import user_type, Alumno
from django.views.generic.list import ListView

from core.models import Encuesta, Pregunta, Categoria, Opcion, Formula, Termino, Rendimiento, Estudio, Asignacion, \
    Alumno
ruta_estudiante = 'core/Estudiante'
def go_estudiante(request):
    if request.user.is_authenticated and user_type.objects.get(user=request.user).es_estudiante:
        alumno=Alumno.objects.filter(usuario=request.user.id).first()
        asignacion = Asignacion.objects.filter(alumno_name=alumno.id).first()
        estudio=Estudio.objects.filter(id=asignacion.estudio.id).first()
        encuesta=Encuesta.objects.filter(id=estudio.encuesta.id).first()
        preguntas=Pregunta.objects.filter(encuesta=encuesta.id)
        opciones=[]
        for pregunta in preguntas:
            opciones.append(list(Opcion.objects.filter(pregunta=pregunta.id)))
        print(opciones)
        return render(request, 'core/Estudiante/home.html',context={'asignacion': asignacion,'alumno':alumno,'encuesta':encuesta,'preguntas':preguntas,'opciones':opciones})
    elif request.user.is_authenticated and user_type.objects.get(user=request.user).es_psicologo:
        return redirect('go_psicologo')
    else:
        return redirect('login')


@login_required
def quiz_detail(request, pk):
    estudio=Estudio.objects.filter(id=pk).first()
    asignacion = Asignacion.objects.filter(estudio=pk).first()
    return render(request, ruta_estudiante + '/home.html',
                  context={'estudio': estudio,'asignacion': asignacion})
