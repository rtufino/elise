from django.contrib import admin
from .models import Alumno, Periodo, Nivel, Carrera, Registro
from import_export import fields, resources
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ForeignKeyWidget
# Register your models here.

class AlumnoResource(resources.ModelResource):
    class Meta:
        model = Alumno

class AlumnoAdmin(ImportExportModelAdmin):
    model = Alumno
    list_display = 'cedula', 'nombres', 'apellidos', 'genero', 'edad', 'ciudad', 'colegio', 'carrera_postular'
    search_fields = ['cedula']
    resource_class = AlumnoResource

class PeriodoAdmin(admin.ModelAdmin):
    model = Periodo
    list_display = 'nombre', 'estado'
    search_fields = ['nombre']

class RegistroResource(resources.ModelResource):
    carrera = fields.Field(
        column_name='carrera',
        attribute='carrera',
        widget=ForeignKeyWidget(Carrera, 'nombre')
    )
    alumno = fields.Field(
        column_name='alumno',
        attribute='alumno',
        widget=ForeignKeyWidget(Alumno, 'cedula')
    )
    periodo = fields.Field(
        column_name='periodo',
        attribute='periodo',
        widget=ForeignKeyWidget(Periodo, 'nombre')
    )
    nivel = fields.Field(
        column_name='nivel',
        attribute='nivel',
        widget=ForeignKeyWidget(Nivel, 'numero')
    )
    nota = fields.Field(
        column_name='nota',
        attribute='nota'
    )
    class Meta:
        model = Registro
        # fields = ('alumno','carrera','periodo','nivel','nota')

class RegistroAdmin(ImportExportModelAdmin):
    # model = Registro
    list_display = 'carrera', 'periodo', 'alumno', 'nivel','nota'
    search_fields = ['carrera', 'periodo']
    resource_class = RegistroResource


admin.site.register(Alumno, AlumnoAdmin)
admin.site.register(Periodo, PeriodoAdmin)
admin.site.register(Nivel)
admin.site.register(Carrera)
admin.site.register(Registro, RegistroAdmin)