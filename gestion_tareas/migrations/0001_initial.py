# Generated by Django 4.1.1 on 2022-09-09 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tarea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(default='', max_length=128)),
                ('fechas_de_creacion', models.CharField(default='', max_length=128)),
                ('fecha_de_entrega', models.CharField(default='', max_length=128)),
                ('usuario_responsable', models.CharField(default='', max_length=128)),
                ('estado_de_tarea', models.CharField(default='', max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='', max_length=128)),
                ('apellido', models.CharField(default='', max_length=128)),
                ('codigo_de_usuario', models.CharField(default='', max_length=128)),
                ('contraseña', models.CharField(default='', max_length=128)),
            ],
        ),
    ]
