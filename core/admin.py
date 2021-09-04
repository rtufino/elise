from django.contrib import admin
from .models import Alumno, Periodo, Nivel, Carrera, Registro
from .models import Encuesta, Categoria, Opcion, Tpregunta, Relacion, Pregunta
from .models import Formula, Evaluacion, Termino, Rendimiento, Parametro, Asignacion, User, Psicologo, \
    Estudio,Respuesta
from import_export import fields, resources
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ForeignKeyWidget
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from simple_history.admin import SimpleHistoryAdmin
from safedelete.admin import SafeDeleteAdmin, highlight_deleted


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
    list_display = (highlight_deleted, 'nombre', 'estado') + SafeDeleteAdmin.list_display
    search_fields = ('nombre', SafeDeleteAdmin.search_fields)


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
    list_display = 'carrera', 'periodo', 'alumno', 'nivel', 'nota'
    search_fields = ['carrera', 'periodo']
    resource_class = RegistroResource


class FormularioAdmin(admin.ModelAdmin):
    readonly_fields = ('nombre')


class CategoriaAdmin(SafeDeleteAdmin):
    model = Categoria
    # list_display = 'nombre', 'siglas'
    # history_list_display = ["status"]
    search_fields = ('nombre', 'siglas') + SafeDeleteAdmin.search_fields
    list_display = (highlight_deleted, "nombre", "siglas") + SafeDeleteAdmin.list_display
    # list_filter = ("last_name",) + SafeDeleteAdmin.list_filter


class EncuestaAdmin(SafeDeleteAdmin):
    model = Encuesta
    list_display = (highlight_deleted, 'nombre', 'f_vigencia', 'estado') + SafeDeleteAdmin.list_display
    search_fields = ('nombre', 'f_vigencia') + SafeDeleteAdmin.search_fields


class OpcionAdmin(SafeDeleteAdmin):
    model = Opcion
    list_display = (highlight_deleted, 'pregunta', 'etiqueta', 'ponderado') + SafeDeleteAdmin.list_display
    search_fields = ('pregunta', 'ponderado') + SafeDeleteAdmin.search_fields


class PreguntaAdmin(SafeDeleteAdmin):
    model = Pregunta
    list_display = (highlight_deleted, 'enunciado', 'tpregunta', 'encuesta', 'categoria') + SafeDeleteAdmin.list_display
    search_fields = ('categoria', 'encuesta', 'enunciado') + SafeDeleteAdmin.search_fields


class InvestigacionAdmin(admin.ModelAdmin):
    readonly_fields = ('alumno')


class AsignacionAdmin(SafeDeleteAdmin):
    model = Asignacion
    list_display = (highlight_deleted, 'alumno_name', 'tipo', 'estudio') + SafeDeleteAdmin.list_display
    search_fields = ('estudio', 'alumno_name') + SafeDeleteAdmin.search_fields


class EstudioAdmin(SafeDeleteAdmin):
    model = Estudio
    list_display = (highlight_deleted, 'observacion', 'encuesta', 'periodo', 'fecha',
                    'id') + SafeDeleteAdmin.list_display
    search_fields = ('periodo', 'observacion') + SafeDeleteAdmin.search_fields


class CarreraAdmin(SafeDeleteAdmin):
    model = Carrera
    list_display = (highlight_deleted, 'id', 'nombre') + SafeDeleteAdmin.list_display
    search_fields = ('nombre', SafeDeleteAdmin.search_fields)


class AlumnoAdmin(admin.ModelAdmin):
    model = Alumno
    list_display = 'cedula', 'usuario', 'nombres', 'apellidos', 'carrera_postular'
    search_fields = ['cedula']


class FormulaAdmin(SafeDeleteAdmin):
    model = Formula
    list_display = (highlight_deleted, 'nombre', 'carrera', 'porcentaje', 'maximo',
                    'minimo') + SafeDeleteAdmin.list_display
    search_fields = ('carrera', 'nombre') + SafeDeleteAdmin.search_fields


class TerminoAdmin(SafeDeleteAdmin):
    model = Termino
    list_display = (highlight_deleted, 'formula', 'variable', 'signo', 'valor') + SafeDeleteAdmin.list_display
    search_fields = ('formula', 'variable') + SafeDeleteAdmin.search_fields


class RendimientoAdmin(SafeDeleteAdmin):
    model = Rendimiento
    list_display = (highlight_deleted, 'formula', 'afinidad', 'rendimiento_satisfactorio',
                    'rendimiento_riesgoso') + SafeDeleteAdmin.list_display
    search_fields = ('formula', 'afinidad') + SafeDeleteAdmin.search_fields


class TipoPregunta(SafeDeleteAdmin):
    model = Tpregunta
    list_display = (highlight_deleted, 'nombre') + SafeDeleteAdmin.list_display
    search_fields = ('nombre', SafeDeleteAdmin.search_fields)


class NivelAdmin(SafeDeleteAdmin):
    model = Nivel
    list_display = (highlight_deleted, 'numero') + SafeDeleteAdmin.list_display
    search_fields = ('numero', SafeDeleteAdmin.search_fields)

class RespuestaAdmin(admin.ModelAdmin):
    model = Respuesta
    list_display = 'categoria', 'asignacion', 'opcion','ponderado','respuesta'
    search_fields = ['asignacion']


admin.site.register(Alumno, AlumnoAdmin)
admin.site.register(Periodo, PeriodoAdmin)
admin.site.register(Nivel, NivelAdmin)
admin.site.register(Carrera, CarreraAdmin)
admin.site.register(Registro, RegistroAdmin)

admin.site.register(Encuesta, EncuestaAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Opcion, OpcionAdmin)
admin.site.register(Tpregunta, TipoPregunta)
admin.site.register(Relacion)
admin.site.register(Pregunta, PreguntaAdmin)
admin.site.register(Estudio, EstudioAdmin)

admin.site.register(Asignacion, AsignacionAdmin)
admin.site.register(Formula, FormulaAdmin)
admin.site.register(Evaluacion)
admin.site.register(Termino, TerminoAdmin)
admin.site.register(Rendimiento, RendimientoAdmin)
admin.site.register(Parametro)
admin.site.register(Psicologo)
admin.site.register(User, UserAdmin)
admin.site.register(Respuesta, RespuestaAdmin)