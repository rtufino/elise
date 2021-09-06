import json
from builtins import print
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from core.models import Encuesta, Pregunta, Categoria, Opcion, Formula, Termino, Rendimiento, Estudio, Asignacion, \
    Alumno, Respuesta, Resultado

ruta_estudiante = 'core/Estudiante'


def resultados(request):
    alumno = Alumno.objects.filter(usuario=request.user.id).first()
    asignacion = Asignacion.objects.filter(alumno_name=alumno.id).first()
    resultado = Resultado.objects.filter(asignacion=asignacion)
    porcentajes_por_carrera = list()
    if resultado:
        print('ya tiene resultado')
        for result in resultado:
            porcentajes_por_carrera.append(
                {
                    'carrera': result.carrera,
                    'afinidad': result.afinidad,
                    'porcentaje': result.porcentaje
                }
            )
    else:
        print('calculando')
        respuestas = Respuesta.objects.filter(asignacion=asignacion)
        formulas = Formula.objects.all()
        formulas_list = list()
        puntaje = 0
        porcentaje = 0

        for formula in formulas:
            terminos = Termino.objects.filter(formula=formula)
            rendimientos = Rendimiento.objects.filter(formula=formula)
            for termino in terminos:
                for respuesta in respuestas:
                    print('se compara ', termino.variable.siglas, ' con ', respuesta.categoria)
                    if termino.variable == respuesta.categoria:
                        print('entra!')
                        puntaje += termino.valor * float(respuesta.ponderado)
                        break

            icav = (puntaje - formula.minimo / formula.maximo - formula.minimo) * 100
            afinidad = False
            if icav > formula.porcentaje:
                for rendimiento in rendimientos:
                    if rendimiento.afinidad:
                        porcentaje = rendimiento.rendimiento_satisfactorio
                        afinidad = True
                        break
            else:
                for rendimiento in rendimientos:
                    if not rendimiento.afinidad:
                        porcentaje = rendimiento.rendimiento_riesgoso
                        afinidad = False
                        break
            porcentajes_por_carrera.append(
                {
                    'carrera': formula.carrera,
                    'afinidad': afinidad,
                    'porcentaje': porcentaje
                }
            )
            formulas_list.append(
                Resultado(
                    asignacion=asignacion,
                    carrera=formula.carrera,
                    porcentaje=porcentaje,
                    afinidad=afinidad
                )
            )
        Resultado.objects.bulk_create(formulas_list)

    return render(request, 'core/Estudiante/resultados.html',
                  context={'porcentajes': porcentajes_por_carrera, 'alumno': alumno})


def go_estudiante(request):
    if request.user.is_authenticated and request.user.is_active and not request.user.is_staff:
        alumno = Alumno.objects.filter(usuario=request.user.id).first()
        if alumno.estado == 0 or alumno.estado == 2:
            return render(request, 'core/Estudiante/validar.html')
        if alumno.encuesta == 1:
            return redirect('go_resultados')
        else:
            asignacion = Asignacion.objects.filter(alumno_name=alumno.id).first()
            estudio = Estudio.objects.filter(id=asignacion.estudio.id).first()
            encuesta = Encuesta.objects.filter(id=estudio.encuesta.id).first()
            preguntas = Pregunta.objects.filter(encuesta=encuesta.id)
            opciones = []
            for pregunta in preguntas:
                opciones.append(list(Opcion.objects.filter(pregunta=pregunta.id)))
            if request.method == "POST":
                print("this is post")
                ponderados = request.POST.getlist('valores')
                respuestas = request.POST.getlist('respuestas')
                opcioncategoria = request.POST.getlist('categorias')
                recopciones = request.POST.getlist('recopciones')
                print(opcioncategoria)
                print(recopciones)
                listresp = []
                for i in range(0, len(ponderados)):
                    categoria = Categoria.objects.get(siglas=opcioncategoria[i])
                    opcion = Opcion.objects.get(id=recopciones[i])
                    print(categoria)
                    respuestas1 = Respuesta(
                        categoria=categoria,
                        asignacion=asignacion,
                        opcion=opcion,
                        ponderado=ponderados[i],
                        respuesta=respuestas[i]
                    )
                    listresp.append(respuestas1)
                Respuesta.objects.bulk_create(listresp)
                alumno.encuesta = '1'
                alumno.save()
                return redirect('go_resultados')
            return render(request, 'core/Estudiante/home.html',
                          context={'asignacion': asignacion, 'alumno': alumno, 'encuesta': encuesta,
                                   'preguntas': preguntas, 'opciones': opciones})
    elif request.user.is_authenticated and request.user.is_staff and request.user.is_active:
        return redirect('go_psicologo')
    else:
        return redirect('login')
