from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone


class UserManager(BaseUserManager):
    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
        if not email:
            raise ValueError('Usuario debe tener un correo ')
        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
            last_login=now,
            date_joined=now,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        return self._create_user(email, password, False, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        user = self._create_user(email, password, True, True, **extra_fields)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=254, unique=True)
    name = models.CharField(max_length=254, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    # def get_absolute_url(self):
    #     return "/users/%i/" % (self.pk)
    def get_email(self):
        return self.email


class user_type(models.Model):
    es_estudiante = models.BooleanField(default=False)
    es_psicologo = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        if self.es_estudiante == True:
            return User.get_email(self.user) + " - es_estudiante"
        else:
            return User.get_email(self.user) + " - es_psicologo"


class Psicologo(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    cedula = models.CharField(max_length=10)

    def __str__(self):
        return self.cedula


class Alumno(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
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
    nombre = models.CharField(max_length=100, verbose_name='Periodo')
    estado = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre


class Nivel(models.Model):
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
    estado = models.IntegerField(default=1)
    f_vigencia = models.DateField(verbose_name='fecha vigencia')
    tipo = models.CharField(max_length=30, default='version 1')
    f_inicio = models.DateField(verbose_name='fecha inicio', auto_now=True)

    def __str__(self):
        return self.nombre


class Categoria(models.Model):
    # id = models.AutoField(primary_key=True)
    calcular = models.BooleanField()
    nombre = models.CharField(max_length=50)
    siglas = models.CharField(max_length=5)
    estado = models.IntegerField(default=1)

    def __str__(self):
        return self.siglas


class Tpregunta(models.Model):
    # id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Pregunta(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    tpregunta = models.ForeignKey(Tpregunta, on_delete=models.CASCADE)
    encuesta = models.ForeignKey(Encuesta, on_delete=models.CASCADE)
    numero = models.IntegerField()
    enunciado = models.CharField(max_length=255)
    estado = models.IntegerField(default=1)

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


class Termino(models.Model):
    # id = models.AutoField(primary_key=True)
    formula = models.ForeignKey(Formula, on_delete=models.CASCADE)
    signo = models.CharField(max_length=5)
    valor = models.FloatField()
    variable = models.ForeignKey(Categoria, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return str(self.valor)


class Rendimiento(models.Model):
    # id = models.AutoField(primary_key=True)
    formula = models.ForeignKey(Formula, on_delete=models.CASCADE)
    rendimiento_satisfactorio = models.FloatField()
    rendimiento_riesgoso = models.FloatField()
    afinidad = models.BooleanField()

    def __str__(self):
        return str(self.formula)


class Parametro(models.Model):
    id = models.AutoField(primary_key=True)
    clave = models.CharField(max_length=100)
    valor = models.CharField(max_length=100)

    def __str__(self):
        return self.clave


class Estudio(models.Model):
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)
    fecha = models.DateField()
    observacion = models.TextField()
    encuesta = models.ForeignKey(Encuesta, on_delete=models.CASCADE)

    def __str__(self):
        return self.periodo.nombre + " " + self.encuesta.nombre


class Asignacion(models.Model):
    # id = models.AutoField(primary_key=True)
    alumno_name = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=30)
    estudio = models.ForeignKey(Estudio, on_delete=models.CASCADE)

    def __str__(self):
        return self.estudio.observacion + " " + self.alumno_name.nombres + " " + self.alumno_name.apellidos
