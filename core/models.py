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