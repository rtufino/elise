from django.contrib import admin
from .models import Encuesta, Categoria, Opcion, Tpregunta, Relacion, Pregunta
# Register your models here.
class FormularioAdmin(admin.ModelAdmin):
    readonly_fields = ('nombre')

class CategoriaAdmin(admin.ModelAdmin):
    model = Categoria
    list_display = 'nombre', 'siglas'
    search_fields = ['nombre', 'siglas']

class EncuestaAdmin(admin.ModelAdmin):
    model = Encuesta
    list_display = 'nombre', 'f_vigencia', 'estado'
    search_fields = ['nombre', 'f_vigencia']

class OpcionAdmin(admin.ModelAdmin):
    model = Opcion
    list_display = 'pregunta', 'etiqueta', 'ponderado'
    search_fields = ['pregunta']

class PreguntaAdmin(admin.ModelAdmin):
    model = Pregunta
    list_display = 'enunciado', 'tpregunta', 'encuesta', 'categoria'
    search_fields = ['categoria', 'encuesta', 'enunciado']

admin.site.register(Encuesta, EncuestaAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Opcion, OpcionAdmin)
admin.site.register(Tpregunta)
admin.site.register(Relacion)
admin.site.register(Pregunta, PreguntaAdmin)