from django.contrib import admin
from .models import Asignacion
# Register your models here.
class InvestigacionAdmin(admin.ModelAdmin):
    readonly_fields = ('alumno')

admin.site.register(Asignacion)