# Generated by Django 3.2 on 2021-09-02 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_pregunta_deleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='formula',
            name='deleted',
            field=models.DateTimeField(editable=False, null=True),
        ),
        migrations.AddField(
            model_name='opcion',
            name='deleted',
            field=models.DateTimeField(editable=False, null=True),
        ),
        migrations.AddField(
            model_name='parametro',
            name='deleted',
            field=models.DateTimeField(editable=False, null=True),
        ),
        migrations.AddField(
            model_name='rendimiento',
            name='deleted',
            field=models.DateTimeField(editable=False, null=True),
        ),
        migrations.AddField(
            model_name='termino',
            name='deleted',
            field=models.DateTimeField(editable=False, null=True),
        ),
    ]
