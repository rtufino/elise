from django.contrib import admin
from .models import Formula, Evaluacion, Termino, Rendimiento, Parametro, Asignacion
# Register your models here.
class InvestigacionAdmin(admin.ModelAdmin):
    readonly_fields = ('alumno')


class AsignacionAdmin(admin.ModelAdmin):
    model = Asignacion
    list_display = 'evaluacion', 'encuesta'
    search_fields = ['encuesta']

admin.site.register(Asignacion, AsignacionAdmin)
admin.site.register(Formula)
admin.site.register(Evaluacion)
admin.site.register(Termino)
admin.site.register(Rendimiento)
admin.site.register(Parametro)