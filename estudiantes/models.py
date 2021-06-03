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

    def __str__(self):
        return self.nombres + "" + self.apellidos

class Periodo(models.Model):
    nombre = models.CharField(max_length=100)
    estado = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre

class Nivel(models.Model):
    numero = models.IntegerField(default=0)

    def __str__(self):
        return self.numero

class Carrera(models.Model):
    nombre= models.CharField(max_length=100)

    def __str__(self):
        return self.numero

class Registro(models.Model):
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)
    nivel = models.ForeignKey(Nivel, on_delete=models.CASCADE)
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    nota = models.FloatField()

    def __str__(self):
        return self.nota