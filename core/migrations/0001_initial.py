# Generated by Django 3.2 on 2021-09-10 02:59

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
                ('es_estudiante', models.BooleanField(default=False)),
                ('es_psicologo', models.BooleanField(default=False)),
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
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('cedula', models.CharField(max_length=10, unique=True)),
                ('nombres', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('genero', models.CharField(max_length=200)),
                ('ciudad', models.CharField(max_length=200)),
                ('colegio', models.CharField(max_length=200)),
                ('edad', models.IntegerField(default=0)),
                ('estado', models.IntegerField(default=1)),
                ('encuesta', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Asignacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('tipo', models.CharField(default='normal', max_length=30)),
                ('completada', models.BooleanField(default=False)),
                ('alumno_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.alumno')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Carrera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('nombre', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('calcular', models.BooleanField()),
                ('nombre', models.CharField(max_length=50)),
                ('siglas', models.CharField(max_length=5)),
                ('estado', models.IntegerField(default=1)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Encuesta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('nombre', models.CharField(max_length=50)),
                ('estado', models.IntegerField(default=1)),
                ('f_vigencia', models.DateField(verbose_name='fecha vigencia')),
                ('tipo', models.CharField(default='version 1', max_length=30)),
                ('f_inicio', models.DateField(auto_now=True, verbose_name='fecha inicio')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Formula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('porcentaje', models.FloatField()),
                ('maximo', models.FloatField()),
                ('minimo', models.FloatField()),
                ('nombre', models.CharField(max_length=100)),
                ('carrera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.carrera')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Nivel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('numero', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Nivel',
                'verbose_name_plural': 'Niveles',
            },
        ),
        migrations.CreateModel(
            name='Opcion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('numero', models.IntegerField()),
                ('ponderado', models.FloatField()),
                ('etiqueta', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Opción',
                'verbose_name_plural': 'Opciones',
            },
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
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('nombre', models.CharField(max_length=100, verbose_name='Periodo')),
                ('estado', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tpregunta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Tipo de Pregunta',
                'verbose_name_plural': 'Tipos de Pregunta',
            },
        ),
        migrations.CreateModel(
            name='Termino',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('valor', models.FloatField()),
                ('formula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.formula')),
                ('variable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.categoria')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Resultado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('afinidad', models.BooleanField()),
                ('porcentaje_s', models.FloatField()),
                ('porcentaje_r', models.FloatField()),
                ('puntaje', models.FloatField(default=0)),
                ('icav', models.FloatField(default=0)),
                ('asignacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.asignacion')),
                ('carrera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.carrera')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Respuesta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('ponderado', models.CharField(default=0, max_length=50)),
                ('respuesta', models.CharField(default='', max_length=250)),
                ('asignacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.asignacion')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.categoria')),
                ('opcion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.opcion')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Rendimiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('rendimiento_satisfactorio', models.FloatField()),
                ('rendimiento_riesgoso', models.FloatField()),
                ('afinidad', models.BooleanField()),
                ('formula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.formula')),
            ],
            options={
                'abstract': False,
            },
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
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('numero', models.IntegerField()),
                ('enunciado', models.TextField()),
                ('estado', models.IntegerField(default=1)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.categoria')),
                ('encuesta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.encuesta')),
                ('tpregunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.tpregunta')),
            ],
            options={
                'abstract': False,
            },
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
            options={
                'verbose_name': 'Evaluación',
                'verbose_name_plural': 'Evaluaciones',
            },
        ),
        migrations.CreateModel(
            name='Estudio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('fecha', models.DateField()),
                ('observacion', models.TextField()),
                ('encuesta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.encuesta')),
                ('periodo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.periodo')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='asignacion',
            name='estudio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.estudio'),
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
