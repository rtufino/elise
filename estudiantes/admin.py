from django.contrib import admin
from .models import Alumno, Periodo, Nivel, Carrera, Registro
# Register your models here.
admin.site.register(Alumno)
admin.site.register(Periodo)
admin.site.register(Nivel)
admin.site.register(Carrera)
admin.site.register(Registro)