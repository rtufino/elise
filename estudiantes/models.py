from django.db import models

# Create your models here.
class Alumno(models.Model):
    cedula = models.CharField(unique=True, max_length=10)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    genero = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=200)
    colegio = models.CharField(max_length=200)
    edad = models.IntegerField(default=0)
    carrera_postular = models.CharField(max_length=200)

    def __str__(self):
        return self.cedula

class Periodo(models.Model):
    # id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name='Periodo')
    estado = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre

class Nivel(models.Model):
    # id = models.AutoField(primary_key=True)
    numero = models.IntegerField(default=0)
    def __str__(self):
        num = str(self.numero)
        return num

class Carrera(models.Model):
    # id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre

class Registro(models.Model):
    # id = models.AutoField(primary_key=True)
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)
    nivel = models.ForeignKey(Nivel, on_delete=models.CASCADE)
    alumno = models.ForeignKey(Alumno, to_field='cedula', on_delete=models.CASCADE)
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    nota = models.FloatField()
    def __str__(self):
        nota = str(self.nota)
        return nota