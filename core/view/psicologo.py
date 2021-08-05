from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from core.models import user_type
from django.urls import reverse_lazy
from core.models import Encuesta, Pregunta, Categoria, Opcion
from core.forms import EncuestaForm, EncuestaDeleteForm, EncuestaUpdateForm, PreguntaForm, CategoriaForm, \
    CategoriaUpdateForm, CategoriaDeleteForm, OpcionForm
from django.views.generic.edit import FormView

ruta_psicologo = 'core/Psicologo'


def go_psicologo(request):
    if request.user.is_authenticated and user_type.objects.get(user=request.user).es_psicologo:
        cantidad_encuestas = Encuesta.objects.count()
        context = {
            'c_encuestas': cantidad_encuestas
        }
        return render(request, ruta_psicologo + '/dashboard.html', context=context)
    elif request.user.is_authenticated and user_type.objects.get(user=request.user).es_estudiante:
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
    # fields = '__all__'
    success_url = reverse_lazy('encuesta')


class EncuestaUpdateView(UpdateView):
    model = Encuesta
    form_class = EncuestaUpdateForm
    # fields = ['nombre', 'f_vigencia']
    template_name = ruta_psicologo + '/encuesta_update_form.html'

    def get_success_url(self):
        return reverse_lazy('encuesta_update', args=[self.object.id]) + '?ok'


class EncuestaDeleteView(UpdateView):
    model = Encuesta
    form_class = EncuestaDeleteForm
    # fields = None
    template_name = ruta_psicologo + '/encuesta_delete_form.html'

    def form_valid(self, form):
        form.instance.estado = 0
        return super().form_valid(form)

    success_url = reverse_lazy('encuesta')


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
        return super().form_valid(form)

    success_url = reverse_lazy('encuesta')

class PreguntaUpdateView(UpdateView):
    model = Pregunta
    form_class = PreguntaForm
    template_name = ruta_psicologo + '/pregunta_update_form.html'

    def form_valid(self, form):
        encuesta_instance = Encuesta.objects.filter(pk=self.object.encuesta.id).first()
        form.instance.encuesta = encuesta_instance
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('pregunta_update', args=[self.object.id]) + '?ok'

def pregunta_detail(request, pk):
    pregunta = Pregunta.objects.filter(id=pk).first()
    opciones = Opcion.objects.filter(pregunta=pk)
    # categorias_preguntas = [pregunta.categoria for pregunta in preguntas]
    # categorias = list(set(categorias_preguntas))
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
    success_url = reverse_lazy('encuesta')


class CategoriaUpdateView(UpdateView):
    model = Categoria
    form_class = CategoriaUpdateForm
    # fields = ['nombre', 'f_vigencia']
    template_name = ruta_psicologo + '/categoria_update_form.html'

    def get_success_url(self):
        return reverse_lazy('categoria_update', args=[self.object.id]) + '?ok'


class CategoriaDeleteView(UpdateView):
    model = Categoria
    form_class = CategoriaDeleteForm
    # fields = None
    template_name = ruta_psicologo + '/categoria_delete_form.html'

    def form_valid(self, form):
        form.instance.estado = 0
        return super().form_valid(form)

    success_url = reverse_lazy('categoria')


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
    form_class = OpcionForm
    template_name = ruta_psicologo + '/opcion_update_form.html'

    def form_valid(self, form):
        pregunta_instance = Pregunta.objects.filter(pk=self.object.pregunta.id).first()
        form.instance.pregunta = pregunta_instance
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('opcion_update', args=[self.object.id]) + '?ok'

# def quiz(request):
#     return render(request, 'core/Psicologo/quiz.html')
#
#
# def question(request, pk):
#     context = {
#         pk: pk
#     }
#     return render(request, 'core/Psicologo/question.html', context)
