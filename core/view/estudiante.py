from builtins import print

from django.contrib.auth.decorators import login_required
from django.http.request import validate_host
from django.shortcuts import render,redirect
from core.models import Alumno
from django.views.generic.list import ListView
from ..decorators import estudiante_required
from core.forms import AnswerRegisterForm

from core.models import Encuesta, Pregunta, Categoria, Opcion, Formula, Termino, Rendimiento, Estudio, Asignacion, \
    Alumno,Respuesta
ruta_estudiante = 'core/Estudiante'


def resultados(request):
    return render(request, 'core/Estudiante/resultados.html')

def go_estudiante(request):
    if request.user.is_authenticated and request.user.is_active and not request.user.is_staff:
        alumno=Alumno.objects.filter(usuario=request.user.id).first()
        asignacion = Asignacion.objects.filter(alumno_name=alumno.id).first()
        estudio=Estudio.objects.filter(id=asignacion.estudio.id).first()
        encuesta=Encuesta.objects.filter(id=estudio.encuesta.id).first()
        preguntas=Pregunta.objects.filter(encuesta=encuesta.id)
        opciones=[]
        for pregunta in preguntas:
            opciones.append(list(Opcion.objects.filter(pregunta=pregunta.id)))
        if request.method=="POST":
            print("this is post")
            ponderados = request.POST.getlist('valores')
            respuestas = request.POST.getlist('respuestas')
            opcioncategoria =request.POST.getlist('categorias')
            asignaciones =Asignacion.objects.get(alumno_name=request.POST.get('asignaciones'))
            recopciones=request.POST.getlist('recopciones')
            print(opcioncategoria)
            print(recopciones)
            listresp=[]
            for i in range(0,len(ponderados)):
                categoria=Categoria.objects.get(siglas=opcioncategoria[i])
                opcion = Opcion.objects.get(id=recopciones[i])
                print(categoria)
                respuestas1 = Respuesta(
                    categoria=categoria,
                    asignacion=asignaciones,
                    opcion=opcion,
                    ponderado=ponderados[i],
                    respuesta=respuestas[i]
                )
                listresp.append(respuestas1)
            Respuesta.objects.bulk_create(listresp)
            return redirect('go_resultados')
        return render(request, 'core/Estudiante/home.html',context={'asignacion': asignacion,'alumno':alumno,'encuesta':encuesta,'preguntas':preguntas,'opciones':opciones})
    elif request.user.is_authenticated and request.user.is_staff and request.user.is_active :
        return redirect('go_psicologo')
    else:
        return redirect('login')

@login_required
def quiz_detail(request, pk):
    estudio=Estudio.objects.filter(id=pk).first()
    asignacion = Asignacion.objects.filter(estudio=pk).first()
    return render(request, ruta_estudiante + '/home.html',
                  context={'estudio': estudio,'asignacion': asignacion})
