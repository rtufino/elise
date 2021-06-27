from django.db import models
from estudiantes.models import Carrera, Alumno, Periodo
from formulario.models import Encuesta
# Create your models here.

class Evaluacion(models.Model):
    # id = models.AutoField(primary_key=True)
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)
    f_inicio = models.TimeField()
    f_fin = models.TimeField()
    tiempo = models.IntegerField(default=0)
    def __str__(self):
        return self.periodo.nombre

class Formula(models.Model):
    # id = models.AutoField(primary_key=True)
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    porcentaje = models.FloatField()
    maximo = models.FloatField()
    minimo = models.FloatField()
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.carrera.nombre


class Asignacion(models.Model):
    # id = models.AutoField(primary_key=True)
    formula = models.ForeignKey(Formula, on_delete=models.CASCADE)
    evaluacion = models.ForeignKey(Evaluacion, on_delete=models.CASCADE)
    alumno_name = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    encuesta = models.ForeignKey(Encuesta, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=30)
    def __str__(self):
        return self.formula.nombre + " " + self.alumno_name.nombres + " " + self.alumno_name.apellidos + " " + self.encuesta.nombre


class Termino(models.Model):
    # id = models.AutoField(primary_key=True)
    formula = models.ForeignKey(Formula, on_delete=models.CASCADE)
    signo = models.CharField(max_length=5)
    valor = models.FloatField()
    def __str__(self):
        return self.formula

class Rendimiento(models.Model):
    # id = models.AutoField(primary_key=True)
    formula = models.ForeignKey(Formula, on_delete=models.CASCADE)
    rendimiento_satisfactorio = models.FloatField()
    rendimiento_riesgoso = models.FloatField()
    afinidad = models.BooleanField()


class Parametro(models.Model):
    id = models.AutoField(primary_key=True)
    clave = models.CharField(max_length=100)
    valor = models.CharField(max_length=100)
    def __str__(self):
        return self.clave