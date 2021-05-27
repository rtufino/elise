# Generated by Django 3.2 on 2021-05-27 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calcular', models.BooleanField()),
                ('nombre', models.CharField(max_length=50)),
                ('siglas', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Encuesta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('estado', models.IntegerField()),
                ('f_vigencia', models.DateTimeField()),
                ('tipo', models.CharField(max_length=30)),
                ('f_inicio', models.DateTimeField()),
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
            name='Tpregunta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Relacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.IntegerField()),
                ('opcion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formulario.opcion')),
            ],
        ),
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
                ('enunciado', models.CharField(max_length=255)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formulario.categoria')),
                ('encuesta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formulario.encuesta')),
                ('tpregunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formulario.tpregunta')),
            ],
        ),
        migrations.AddField(
            model_name='opcion',
            name='pregunta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formulario.pregunta'),
        ),
        migrations.CreateModel(
            name='Asignacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=30)),
                ('encuesta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formulario.encuesta')),
            ],
        ),
    ]
