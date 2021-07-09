from django.contrib import admin
from .models import Alumno, Periodo, Nivel, Carrera, Registro
from .models import Encuesta, Categoria, Opcion, Tpregunta, Relacion, Pregunta
from .models import Formula, Evaluacion, Termino, Rendimiento, Parametro, Asignacion,User,user_type,Psicologo
from import_export import fields, resources
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ForeignKeyWidget
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password', 'name', 'last_login')}),
        ('Permissions', {'fields': (
            'is_active',
            'is_staff',
            'is_superuser',
            'groups',
            'user_permissions',
        )}),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('email', 'password1', 'password2')
            }
        ),
    )

    list_display = ('email', 'name', 'is_staff', 'last_login')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)

class AlumnoResource(resources.ModelResource):
    class Meta:
        model = Alumno


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


admin.site.register(Alumno)
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
admin.site.register(Psicologo)
admin.site.register(User, UserAdmin)
admin.site.register(user_type)
