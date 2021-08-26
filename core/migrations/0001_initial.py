# Generated by Django 3.2 on 2021-08-20 04:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('name', models.CharField(blank=True, max_length=254, null=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.CharField(max_length=10, unique=True)),
                ('nombres', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('genero', models.CharField(max_length=200)),
                ('ciudad', models.CharField(max_length=200)),
                ('colegio', models.CharField(max_length=200)),
                ('edad', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Carrera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calcular', models.BooleanField()),
                ('nombre', models.CharField(max_length=50)),
                ('siglas', models.CharField(max_length=5)),
                ('estado', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Encuesta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('estado', models.IntegerField(default=1)),
                ('f_vigencia', models.DateField(verbose_name='fecha vigencia')),
                ('tipo', models.CharField(default='version 1', max_length=30)),
                ('f_inicio', models.DateField(auto_now=True, verbose_name='fecha inicio')),
            ],
        ),
        migrations.CreateModel(
            name='Formula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('porcentaje', models.FloatField()),
                ('maximo', models.FloatField()),
                ('minimo', models.FloatField()),
                ('nombre', models.CharField(max_length=100)),
                ('carrera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.carrera')),
            ],
        ),
        migrations.CreateModel(
            name='Nivel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Opcion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
                ('ponderado', models.FloatField()),
                ('etiqueta', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Parametro',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('clave', models.CharField(max_length=100)),
                ('valor', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Periodo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Periodo')),
                ('estado', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Tpregunta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='user_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('es_estudiante', models.BooleanField(default=False)),
                ('es_psicologo', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Termino',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('signo', models.CharField(max_length=5)),
                ('valor', models.FloatField()),
                ('formula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.formula')),
                ('variable', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='core.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Rendimiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rendimiento_satisfactorio', models.FloatField()),
                ('rendimiento_riesgoso', models.FloatField()),
                ('afinidad', models.BooleanField()),
                ('formula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.formula')),
            ],
        ),
        migrations.CreateModel(
            name='Relacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.IntegerField()),
                ('opcion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.opcion')),
            ],
        ),
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.FloatField()),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.alumno', to_field='cedula')),
                ('carrera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.carrera')),
                ('nivel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.nivel')),
                ('periodo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.periodo')),
            ],
        ),
        migrations.CreateModel(
            name='Psicologo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.CharField(max_length=10)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
                ('enunciado', models.CharField(max_length=255)),
                ('estado', models.IntegerField(default=1)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.categoria')),
                ('encuesta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.encuesta')),
                ('tpregunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.tpregunta')),
            ],
        ),
        migrations.AddField(
            model_name='opcion',
            name='pregunta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.pregunta'),
        ),
        migrations.CreateModel(
            name='Evaluacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_inicio', models.TimeField()),
                ('f_fin', models.TimeField()),
                ('tiempo', models.IntegerField(default=0)),
                ('periodo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.periodo')),
            ],
        ),
        migrations.CreateModel(
            name='Estudio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('observacion', models.TextField()),
                ('encuesta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.encuesta')),
                ('periodo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.periodo')),
            ],
        ),
        migrations.CreateModel(
            name='Asignacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(default='normal', max_length=30)),
                ('alumno_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.alumno')),
                ('estudio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.estudio')),
            ],
        ),
        migrations.AddField(
            model_name='alumno',
            name='carrera_postular',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.carrera'),
        ),
        migrations.AddField(
            model_name='alumno',
            name='usuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
