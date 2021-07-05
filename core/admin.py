from django.contrib import admin
from .models import Alumno, Periodo, Nivel, Carrera, Registro
from .models import Encuesta, Categoria, Opcion, Tpregunta, Relacion, Pregunta
from .models import Formula, Evaluacion, Termino, Rendimiento, Parametro, Asignacion,Usuario,Psicologo

from import_export import fields, resources
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ForeignKeyWidget
# Register your models here.

class AlumnoResource(resources.ModelResource):
    class Meta:
        model = Alumno

class PsicologoAdmin(admin.ModelAdmin):
    model = Psicologo
    list_display = ('cedula', 'get_apellido', 'get_nombre', 'es_psicologo')

    def get_nombre(self, obj):
        return obj.usuario.first_name

    def get_apellido(self, obj):
        return obj.usuario.last_name

    def es_psicologo(self, obj):
        return obj.usuario.es_psicologo

    es_psicologo.boolean = True

    get_nombre.short_description = 'Nombres'
    get_apellido.short_description = 'Apellidos'
    es_psicologo.short_description = 'Psicologo'
    get_nombre.admin_order_field = 'usuario__first_name'
    get_apellido.admin_order_field = 'usuario__last_name'
    list_filter = ('usuario__is_active', 'usuario__es_psicologo')
class AlumnoAdmin(ImportExportModelAdmin):
    model = Alumno
    list_display = 'cedula', 'nombres', 'apellidos', 'genero', 'edad', 'ciudad', 'colegio', 'carrera_postular'
    search_fields = ['cedula']
    # resource_class = AlumnoResource
    def get_nombre(self, obj):
        return obj.usuario.first_name

    def get_apellido(self, obj):
        return obj.usuario.last_name

    get_nombre.short_description = 'Nombres'
    get_apellido.short_description = 'Apellidos'
    get_nombre.admin_order_field = 'usuario__first_name'
    get_apellido.admin_order_field = 'usuario__last_name'
    list_filter = ('usuario__is_active',)

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

class InvestigacionAdmin(admin.ModelAdmin):
    readonly_fields = ('alumno')


class AsignacionAdmin(admin.ModelAdmin):
    model = Asignacion
    list_display = 'evaluacion', 'encuesta'
    search_fields = ['encuesta']


admin.site.register(Alumno, AlumnoAdmin)
admin.site.register(Periodo, PeriodoAdmin)
admin.site.register(Nivel)
admin.site.register(Carrera)
admin.site.register(Registro, RegistroAdmin)

admin.site.register(Encuesta, EncuestaAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Opcion, OpcionAdmin)
admin.site.register(Tpregunta)
admin.site.register(Relacion)
admin.site.register(Pregunta, PreguntaAdmin)

admin.site.register(Asignacion, AsignacionAdmin)
admin.site.register(Formula)
admin.site.register(Evaluacion)
admin.site.register(Termino)
admin.site.register(Rendimiento)
admin.site.register(Parametro)
admin.site.register(Usuario)
admin.site.register(Psicologo,PsicologoAdmin)