from django.db import models

# Create your models here.
class Alumno(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    genero = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=200)
    colegio = models.CharField(max_length=200)
    edad = models.IntegerField(default=0)
    carrera_postular = models.CharField(max_length=200)

class Periodo(models.Model):
    nombre = models.CharField(max_length=100)
    estado = models.IntegerField(default=0)

class Nivel(models.Model):
    numero = models.IntegerField(default=0)

class Carrera(models.Model):
    nombre = models.CharField(max_length=100)

class Registro(models.Model):
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)
    nivel = models.ForeignKey(Nivel, on_delete=models.CASCADE)
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    carrera = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    nota = models.FloatField()