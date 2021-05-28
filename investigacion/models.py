from django.db import models
from estudiantes.models import Carrera, Alumno, Periodo
from formulario.models import Encuesta
# Create your models here.

class Evaluacion(models.Model):
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)
    f_inicio=models.TimeField()
    f_fin = models.TimeField()
    tiempo = models.IntegerField(default=0)

class Formula(models.Model):
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    porcentaje = models.FloatField()
    maximo =models.FloatField()
    minimo = models.FloatField()
    nombre = models.CharField(max_length=100)

class Asignacion(models.Model):
    formula = models.ForeignKey(Formula, on_delete=models.CASCADE)
    evaluacion = models.ForeignKey(Evaluacion, on_delete=models.CASCADE)
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    encuesta = models.ForeignKey(Encuesta, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=30)

class Termino(models.Model):
    formula = models.ForeignKey(Formula, on_delete=models.CASCADE)
    signo = models.CharField(max_length=5)
    valor = models.FloatField()

class Rendimiento(models.Model):
    formula = models.ForeignKey(Formula, on_delete=models.CASCADE)
    rendimiento_satisfactorio= models.FloatField()
    rendimiento_riesgoso = models.FloatField()
    afinidad =models.BooleanField()

class Parametro(models.Model):
    clave = models.CharField(max_length=100)
    valor = models.CharField(max_length=100)