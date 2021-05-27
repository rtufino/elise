from django.db import models

# Create your models here.
class Encuesta(models.Model):
    nombre = models.CharField(max_length=50)
    estado = models.IntegerField()
    f_vigencia = models.DateTimeField(verbose_name='fecha vigencia')
    tipo = models.CharField(max_length=30)
    f_inicio = models.DateTimeField()
    class Meta:
        verbose_name = 'Encuesta'
    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    calcular = models.BooleanField()
    nombre = models.CharField(max_length=50)
    siglas = models.CharField(max_length=5)


class Tpregunta(models.Model):
    nombre = models.CharField(max_length=50)

class Pregunta(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    tpregunta = models.ForeignKey(Tpregunta, on_delete=models.CASCADE)
    encuesta = models.ForeignKey(Encuesta, on_delete=models.CASCADE)
    numero = models.IntegerField()
    enunciado = models.CharField(max_length=255)

class Opcion(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    numero = models.IntegerField()
    ponderado = models.FloatField()
    etiqueta = models.CharField(max_length=30)

class Relacion(models.Model):
    opcion = models.ForeignKey(Opcion, on_delete=models.CASCADE)
    estado = models.IntegerField()