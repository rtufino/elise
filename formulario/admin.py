from django.contrib import admin
from .models import Encuesta, Categoria, Opcion, Tpregunta, Relacion, Pregunta
# Register your models here.
class FormularioAdmin(admin.ModelAdmin):
    readonly_fields = ('nombre')

admin.site.register(Encuesta)
admin.site.register(Categoria)
admin.site.register(Opcion)
admin.site.register(Tpregunta)
admin.site.register(Relacion)
admin.site.register(Pregunta)