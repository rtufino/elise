from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.db.models import Count, Sum, F
from django.db import models
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from core.models import Encuesta, Pregunta, Categoria, Opcion, Formula, Termino, Rendimiento, Estudio, Asignacion, \
    Alumno, Carrera, Respuesta
from core.forms import EncuestaForm, EncuestaDeleteForm, EncuestaUpdateForm, PreguntaForm, PreguntaUpdateForm, \
    CategoriaForm, \
    CategoriaUpdateForm, CategoriaDeleteForm, OpcionForm, OpcionUpdateForm
from core.auto_choices import addChoices

from django.forms.models import inlineformset_factory

ruta_psicologo = 'core/Psicologo'


def go_psicologo(request):
    if request.user.is_authenticated and request.user.is_staff and request.user.is_active:
        estudios = Estudio.objects.all()
        context = {}
        if request.method == "POST":
            estudio_id = request.POST.get('estudio_select')
            estudio = Estudio.objects.filter(id=estudio_id).first()
            asignaciones = Asignacion.objects.filter(estudio=estudio)
            conteo_asignaciones = asignaciones.count()
            asignaciones_completadas = asignaciones.filter(completada=True).count()
            # lel = Respuesta.objects.all().aggregate(Sum('amount'))['amount__sum'] or 0.00
            if asignaciones_completadas != 0:
                respuestas = Respuesta.objects.all()
                cat = []
                punt = []
                asg = []
                cant = []
                for respuesta in respuestas:
                    if respuesta.categoria.nombre not in cat:
                        cat.append(respuesta.categoria.nombre)
                        punt.append(respuesta.ponderado)
                    else:
                        indice = cat.index(respuesta.categoria.nombre)
                        ponderado_anterior = float(punt[indice]) + float(respuesta.ponderado)
                        punt[indice] = ponderado_anterior
                for asignacion in asignaciones:
                    if asignacion.alumno_name.carrera_postular.nombre not in asg:
                        asg.append(asignacion.alumno_name.carrera_postular.nombre)
                        cant.append(1)
                    else:
                        indice = asg.index(asignacion.alumno_name.carrera_postular.nombre)
                        cant_anterior = cant[indice] + 1
                        cant[indice] = cant_anterior

                # categorias_x_estudio = list(Respuesta.objects.all().values('categoria__nombre').annotate(
                #     totalp=Sum(('ponderado'), output_field=models.FloatField())))
                #
                # carreras_x_estudio = list(
                #     Asignacion.objects.all().values('alumno_name__carrera_postular__nombre').annotate(
                #         number=Count('alumno_name')))
                categoriasXestudio = []
                carrerasXestudio = []
                for o in range(0, len(cat)):
                    categoriasXestudio.append(
                        {
                            'categoria': cat[o],
                            'totalp': punt[o]
                        }
                    )
                for i in range(0, len(asg)):
                    carrerasXestudio.append(
                        {
                            'carrera': asg[i],
                            'postulantes': cant[i]
                        }
                    )
                # print('new carrrers', carrerasXestudio)
                # print('new categroies: ', categoriasXestudio)
            else:
                categoriasXestudio = []
                carrerasXestudio = []
            context = {
                'estudios': estudios,
                'asignaciones': conteo_asignaciones,
                'asig_completas': asignaciones_completadas,
                'consulta': categoriasXestudio,
                'carreras_participantes': carrerasXestudio,
                'este_estudio': estudio
            }
        else:
            context = {
                'estudios': estudios,
                'asignaciones': '--',
                'asig_completas': '--',
                'consulta': '--',
                'carreras_participantes': '--',
                'este_estudio': 'ninguna selección'
            }
        return render(request, ruta_psicologo + '/dashboard.html', context=context)
    elif request.user.is_authenticated and request.user.is_active and not request.user.is_staff:
        return redirect('go_estudiante')
    else:
        return redirect('login')


# Encuestas
class EncuestaListView(ListView):
    model = Encuesta
    template_name = ruta_psicologo + '/encuesta_list.html'


class EncuestaCreateView(CreateView):
    model = Encuesta
    form_class = EncuestaForm
    template_name = ruta_psicologo + '/encuesta_form.html'
    success_url = reverse_lazy('encuesta')


class EncuestaUpdateView(UpdateView):
    model = Encuesta
    form_class = EncuestaUpdateForm
    # fields = ['nombre', 'f_vigencia']
    template_name = ruta_psicologo + '/encuesta_update_form.html'

    def get_success_url(self):
        return reverse_lazy('encuesta_update', args=[self.object.id]) + '?ok'


class EncuestaDeleteView(DeleteView):
    model = Encuesta
    template_name = ruta_psicologo + '/encuesta_delete_form.html'

    success_url = reverse_lazy('encuesta')
    # def get_success_url(self):
    #     print(self.object.encuesta)
    #     return reverse_lazy('encuesta', args=[self.object.encuesta.id])


def encuesta_detail(request, pk):
    encuesta = Encuesta.objects.filter(id=pk).first()
    preguntas = Pregunta.objects.filter(encuesta=pk)
    categorias_preguntas = [pregunta.categoria for pregunta in preguntas]
    categorias = list(set(categorias_preguntas))
    return render(request, ruta_psicologo + '/encuesta_detail.html',
                  context={'preguntas': preguntas, 'categorias': categorias, 'encuesta': encuesta})


class PreguntaCreateView(CreateView):
    model = Pregunta
    form_class = PreguntaForm
    template_name = ruta_psicologo + '/pregunta_form.html'

    def form_valid(self, form):
        encuesta_instance = Encuesta.objects.filter(pk=self.kwargs.get('pk')).first()
        form.instance.encuesta = encuesta_instance
        pregunta = form.save()
        addChoices(pregunta)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('encuesta_detalle', args=[self.object.encuesta.id])
    # success_url = reverse_lazy('encuesta')


class PreguntaUpdateView(UpdateView):
    model = Pregunta
    form_class = PreguntaUpdateForm
    template_name = ruta_psicologo + '/pregunta_update_form.html'

    def get_success_url(self):
        return reverse_lazy('pregunta_update', args=[self.object.id]) + '?ok'


class PreguntaDeleteView(DeleteView):
    model = Pregunta
    template_name = ruta_psicologo + '/pregunta_delete_form.html'

    def get_success_url(self):
        print(self.object.encuesta)
        return reverse_lazy('encuesta_detalle', args=[self.object.encuesta.id])


def pregunta_detail(request, pk):
    pregunta = Pregunta.objects.filter(id=pk).first()
    opciones = Opcion.objects.filter(pregunta=pk)
    return render(request, ruta_psicologo + '/pregunta_detail.html',
                  context={'pregunta': pregunta, 'opciones': opciones})


class CategoriaListView(ListView):
    model = Categoria
    template_name = ruta_psicologo + '/categoria_list.html'


class CategoriaCreateView(CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = ruta_psicologo + '/categoria_form.html'
    # fields = '__all__'
    success_url = reverse_lazy('categoria')


class CategoriaUpdateView(UpdateView):
    model = Categoria
    form_class = CategoriaUpdateForm
    # fields = ['nombre', 'f_vigencia']
    template_name = ruta_psicologo + '/categoria_update_form.html'

    def get_success_url(self):
        return reverse_lazy('categoria_update', args=[self.object.id]) + '?ok'


class CategoriaDeleteView(DeleteView):
    model = Categoria
    template_name = ruta_psicologo + '/categoria_delete_form.html'
    success_url = reverse_lazy('categoria')
    # def get_success_url(self):
    #     print(self.object.encuesta)
    #     return reverse_lazy('cate', args=[self.object.encuesta.id])


class OpcionCreateView(CreateView):
    model = Opcion
    form_class = OpcionForm
    template_name = ruta_psicologo + '/opcion_form.html'

    def form_valid(self, form):
        pregunta_instance = Pregunta.objects.filter(pk=self.kwargs.get('pk')).first()
        form.instance.pregunta = pregunta_instance
        return super().form_valid(form)

    # success_url = reverse_lazy('encuesta')
    def get_success_url(self):
        return reverse_lazy('pregunta_detalle', args=[self.kwargs.get('pk')])


class OpcionUpdateView(UpdateView):
    model = Opcion
    form_class = OpcionUpdateForm
    template_name = ruta_psicologo + '/opcion_update_form.html'

    def get_success_url(self):
        return reverse_lazy('opcion_update', args=[self.object.id]) + '?ok'


class OpcionDeleteView(DeleteView):
    model = Opcion
    template_name = ruta_psicologo + '/opcion_delete_form.html'

    def get_success_url(self):
        print(self.object.pregunta.id)
        return reverse_lazy('pregunta_detalle', args=[self.object.pregunta.id])


class FormulaListView(ListView):
    model = Formula
    template_name = ruta_psicologo + '/formula_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        queryset = object_list if object_list is not None else self.object_list
        page_size = self.get_paginate_by(queryset)
        context_object_name = self.get_context_object_name(queryset)
        objects = []
        terminos = []
        rendimientos = []
        # formula = []
        for formula in queryset:
            termino_instance = Termino.objects.filter(formula=formula.id)
            rendimiento_instance = Rendimiento.objects.filter(formula=formula.id)
            # formula.append(f)
            for i in range(0, len(termino_instance)):
                terminos.append(termino_instance[i])
            for i in range(0, len(rendimiento_instance)):
                rendimientos.append(rendimiento_instance[i])
            objects.append({'formula': formula, 'termino': terminos, 'rend': rendimientos})
            terminos = []
            rendimientos = []
        if page_size:
            paginator, page, queryset, is_paginated = self.paginate_queryset(queryset, page_size)
            context = {
                'paginator': paginator,
                'page_obj': page,
                'is_paginated': is_paginated,
                'object_list': queryset
            }
        else:
            context = {
                'paginator': None,
                'page_obj': None,
                'is_paginated': False,
                'object_list': queryset,
                'terms_list': objects
            }
        if context_object_name is not None:
            context[context_object_name] = queryset
        context.update(kwargs)
        return super().get_context_data(**context)


RendimientoFormset = inlineformset_factory(
    Formula, Rendimiento, fields=('__all__'), max_num=2, extra=2
)

TerminoFormset = inlineformset_factory(
    Formula, Termino, fields=('__all__'), extra=1
)


class FormulaCreateView(CreateView):
    model = Formula
    fields = '__all__'
    template_name = ruta_psicologo + '/formula_form.html'

    def get_context_data(self, **kwargs):
        # we need to overwrite get_context_data
        # to make sure that our formset is rendered
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data["termino"] = TerminoFormset(self.request.POST)
            data["rendimiento"] = RendimientoFormset(self.request.POST)
        else:
            data["termino"] = TerminoFormset()
            data["rendimiento"] = RendimientoFormset()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        termino = context["termino"]
        rendimiento = context["rendimiento"]
        self.object = form.save()
        if termino.is_valid() and rendimiento.is_valid():
            termino.instance = self.object
            rendimiento.instance = self.object
            termino.save()
            rendimiento.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('formula')


class FormulaUpdateView(UpdateView):
    model = Formula
    fields = '__all__'
    template_name = ruta_psicologo + '/formula_update_form.html'

    def get_context_data(self, **kwargs):
        # we need to overwrite get_context_data
        # to make sure that our formset is rendered.
        # the difference with CreateView is that
        # on this view we pass instance argument
        # to the formset because we already have
        # the instance created
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data["termino"] = TerminoFormset(self.request.POST, instance=self.object)
            data["rendimiento"] = RendimientoFormset(self.request.POST, instance=self.object)
        else:
            data["termino"] = TerminoFormset(instance=self.object)
            data["rendimiento"] = RendimientoFormset(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        termino = context["termino"]
        rendimiento = context["rendimiento"]
        self.object = form.save()
        if termino.is_valid() or rendimiento.is_valid():
            termino.instance = self.object
            rendimiento.instance = self.object
            rendimiento.save()
            termino.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('formula')


class FormulaDeleteView(DeleteView):
    model = Formula
    template_name = ruta_psicologo + '/formula_delete_form.html'

    success_url = reverse_lazy('formula')


class EstudioListView(ListView):
    model = Estudio
    template_name = ruta_psicologo + '/estudio_list.html'


class EstudioCreateView(CreateView):
    model = Estudio
    fields = '__all__'
    template_name = ruta_psicologo + '/estudio_form.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            # Book.objects.filter(name__startswith="Django").annotate(num_authors=Count('authors'))
            data["carreras"] = Carrera.objects.filter(alumno__estado=1).annotate(number_of_students=Count('alumno'))
            # data["carreras"] = Carrera.objects.annotate(number_of_students=Count('alumno'))
        else:
            data["carreras"] = Carrera.objects.filter(alumno__estado=1).annotate(number_of_students=Count('alumno'))
            # data["carreras"] = Carrera.objects.annotate(number_of_students=Count('alumno'))
        return data

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = self.get_form()
            if form.is_valid():
                estudio = form.save()
                carreras_a_estudiar = request.POST.getlist("estudio_name")
                alumnos_postulantes = Alumno.objects.filter(carrera_postular__in=carreras_a_estudiar)
                asignacion_list = list()
                for postulante in alumnos_postulantes:
                    if postulante.estado == 1:
                        asignacion_list.append(
                            Asignacion(
                                alumno_name=postulante,
                                tipo="asignacion automatica",
                                estudio=estudio
                            )
                        )
                Asignacion.objects.bulk_create(asignacion_list)

                return self.form_valid(form)
            else:
                return self.form_invalid(form)

    success_url = reverse_lazy('estudio')


class EstudioDeleteView(DeleteView):
    model = Estudio
    template_name = ruta_psicologo + '/estudio_delete_form.html'
    success_url = reverse_lazy('estudio')
