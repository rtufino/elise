from django.db import models

# Create your models here.
class Encuesta(models.Model):
    # id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    estado = models.IntegerField()
    f_vigencia = models.DateTimeField(verbose_name='fecha vigencia')
    tipo = models.CharField(max_length=30)
    f_inicio = models.DateTimeField(verbose_name='fecha inicio')
    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    # id = models.AutoField(primary_key=True)
    calcular = models.BooleanField()
    nombre = models.CharField(max_length=50)
    siglas = models.CharField(max_length=5)
    def __str__(self):
        return self.nombre


class Tpregunta(models.Model):
    # id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

class Pregunta(models.Model):
    # id = models.AutoField(primary_key=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    tpregunta = models.ForeignKey(Tpregunta, on_delete=models.CASCADE)
    encuesta = models.ForeignKey(Encuesta, on_delete=models.CASCADE)
    numero = models.IntegerField()
    enunciado = models.CharField(max_length=255)
    def __str__(self):
        return self.enunciado

class Opcion(models.Model):
    # id = models.AutoField(primary_key=True)
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    numero = models.IntegerField()
    ponderado = models.FloatField()
    etiqueta = models.CharField(max_length=30)
    def __str__(self):
        return self.etiqueta

class Relacion(models.Model):
    # id = models.AutoField(primary_key=True)
    opcion = models.ForeignKey(Opcion, on_delete=models.CASCADE)
    estado = models.IntegerField()
    def __str__(self):
        return self.opcion.etiqueta