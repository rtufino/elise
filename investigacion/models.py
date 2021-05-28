from django.db import models
from estudiantes.models import Carrera, Alumno, Periodo
from formulario.models import Encuesta, Categoria
# Create your models here.

class Evaluacion(models.Model):
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)
    f_inicio=models.TimeField()
    f_fin = models.TimeField()
    tiempo = models.IntegerField(default=0)

class Formula(models.Model):
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    porcentaje = models.DecimalField(decimal_places=10,max_digits=6)
    maximo = models.DecimalField(decimal_places=10,max_digits=6)
    minimo = models.DecimalField(decimal_places=10,max_digits=6)
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
    valor = models.DecimalField(decimal_places=10,max_digits=10)

class Rendimiento(models.Model):
    formula = models.ForeignKey(Formula, on_delete=models.CASCADE)
    rendimiento_satisfactorio= models.DecimalField(decimal_places=10)
    rendimiento_riesgoso = models.DecimalField(decimal_places=10,max_digits=10)
    afinidad =models.BooleanField()

class formula_categoria(models.Model):
    formula = models.ForeignKey(Formula, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

class Parametro(models.Model):
    clave = models.CharField(max_length=100)
    valor = models.CharField(max_length=100)