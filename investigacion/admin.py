from django.contrib import admin
from .models import Asignacion, Formula, Evaluacion, Termino, Rendimiento, Parametro
# Register your models here.
class InvestigacionAdmin(admin.ModelAdmin):
    readonly_fields = ('alumno')

admin.site.register(Asignacion)
admin.site.register(Formula)
admin.site.register(Evaluacion)
admin.site.register(Termino)
admin.site.register(Rendimiento)
admin.site.register(Parametro)