from django.contrib import admin
from .models import Alumno, Periodo, Nivel, Carrera, Registro
# Register your models here.

class AlumnoAdmin(admin.ModelAdmin):
    model = Alumno
    list_display = 'nombres', 'apellidos', 'genero', 'edad', 'ciudad', 'colegio', 'carrera_postular'
    search_fields = ['nombres']

class PeriodoAdmin(admin.ModelAdmin):
    model = Periodo
    list_display = 'nombre', 'estado'
    search_fields = ['nombre']

class RegistroAdmin(admin.ModelAdmin):
    model = Registro
    list_display = 'carrera', 'periodo', 'alumno', 'nota'
    search_fields = ['carrera', 'periodo']


admin.site.register(Alumno, AlumnoAdmin)
admin.site.register(Periodo, PeriodoAdmin)
admin.site.register(Nivel)
admin.site.register(Carrera)
admin.site.register(Registro, RegistroAdmin)