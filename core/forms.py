from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Encuesta, Pregunta, Tpregunta, Categoria, Opcion, Asignacion, Alumno


class AnswerRegisterForm(forms.Form):
    CHOICES = [('M', 'Male'), ('F', 'Female')]
    Gender = forms.CharField(label='Gender', widget=forms.RadioSelect(choices=CHOICES))
    name = forms.CharField(label='name')


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# Encuestas
class EncuestaForm(forms.ModelForm):
    class Meta:
        model = Encuesta
        fields = ['nombre', 'f_vigencia']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'f_vigencia': forms.TextInput(attrs={'class': 'form-control'}),
            # 'f_inicio': forms.DateInput(attrs={'type': 'date'}),
            # 'estado': forms.TextInput(attrs={'class': 'form-control'}),
            # 'tipo': forms.TextInput(attrs={'class': 'form-control'}),
        }


class EncuestaUpdateForm(forms.ModelForm):
    class Meta:
        model = Encuesta
        fields = ['nombre', 'f_vigencia']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'f_vigencia': forms.TextInput(attrs={'class': 'form-control'}),
        }


class EncuestaDeleteForm(forms.ModelForm):
    class Meta:
        model = Encuesta
        fields = ['nombre', 'f_vigencia']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control-plaintext', 'readonly': ''}),
            'f_vigencia': forms.TextInput(attrs={'class': 'd-none'}),
            # 'f_inicio': forms.DateInput(attrs={'type': 'date'}),
            # 'estado': forms.TextInput(attrs={'class': 'form-control'}),
            # 'tipo': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'nombre': '', 'f_vigencia': ''
        }


## Preguntas
class PreguntaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PreguntaForm, self).__init__(*args, **kwargs)
        encuesta = Encuesta.objects.first()
        self.initial['encuesta'] = encuesta

    class Meta:
        model = Pregunta
        fields = ['enunciado', 'numero', 'tpregunta', 'encuesta', 'categoria']
        widgets = {
            'enunciado': forms.TextInput(attrs={'class': 'form-control'}),
            'numero': forms.NumberInput(attrs={'class': 'form-control'}),
            'tpregunta': forms.Select(attrs={'class': 'form-control'}),
            'encuesta': forms.Select(attrs={'class': 'form-control d-none'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'encuesta': ''
        }


class PreguntaUpdateForm(forms.ModelForm):
    class Meta:
        model = Pregunta
        fields = ['enunciado', 'numero', 'tpregunta', 'encuesta', 'categoria']
        widgets = {
            'enunciado': forms.TextInput(attrs={'class': 'form-control'}),
            'numero': forms.NumberInput(attrs={'class': 'form-control'}),
            'tpregunta': forms.Select(attrs={'class': 'form-control'}),
            'encuesta': forms.Select(attrs={'class': 'form-control d-none'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'encuesta': ''
        }


## Categorias

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'siglas': forms.TextInput(attrs={'class': 'form-control'}),
            'calcular': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'estado': forms.TextInput(attrs={'class': 'd-none'})
        }
        labels = {
            'estado': ''
        }


class CategoriaUpdateForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'siglas': forms.TextInput(attrs={'class': 'form-control'}),
            'calcular': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'estado': forms.TextInput(attrs={'class': 'd-none'})
        }
        labels = {
            'estado': ''
        }


class CategoriaDeleteForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control-plaintext', 'readonly': ''}),
            # 'nombre': forms.TextInput(attrs={'class': 'd-none'}),
            'siglas': forms.TextInput(attrs={'class': 'd-none'}),
            'calcular': forms.CheckboxInput(attrs={'class': 'd-none'}),
        }
        labels = {
            'nombre': '', 'siglas': '', 'calcular': ''
        }


## Opciones
class OpcionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(OpcionForm, self).__init__(*args, **kwargs)
        pregunta = Pregunta.objects.first()
        self.initial['pregunta'] = pregunta

    class Meta:
        model = Opcion
        fields = '__all__'
        widgets = {
            'pregunta': forms.Select(attrs={'class': 'form-control d-none'}),
            'numero': forms.NumberInput(attrs={'class': 'form-control'}),
            'ponderado': forms.NumberInput(attrs={'class': 'form-control'}),
            'etiqueta': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'pregunta': ''
        }


class OpcionUpdateForm(forms.ModelForm):
    class Meta:
        model = Opcion
        fields = '__all__'
        widgets = {
            'pregunta': forms.Select(attrs={'class': 'form-control d-none'}),
            'numero': forms.NumberInput(attrs={'class': 'form-control'}),
            'ponderado': forms.NumberInput(attrs={'class': 'form-control'}),
            'etiqueta': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'pregunta': ''
        }

# class AsignacionForm(forms.ModelForm):
#     class Meta:
#         model = Asignacion
#         fields = '__all__'
#
#         def __init__(self, *args, **kwargs):
#             super(AsignacionForm, self).__init__(*args, **kwargs)
#             alumno = str(Alumno.objects.all().first())
#             self.fields['alumno_name'] = forms.CharField(empty_value=alumno)
#             # self.fields['alumno_name'] = forms.IntegerField(label='How much to sent?',
#             #                                                 required=True,
#             #                                                 max_value=curmax,
#             #                                                 min_value=0,
#             #                                                 )
