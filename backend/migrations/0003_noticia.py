# Generated by Django 4.1.7 on 2023-03-03 17:04

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_carrera'),
    ]

    operations = [
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id_noticia', models.AutoField(primary_key=True, serialize=False)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('titulo', models.CharField(max_length=150)),
                ('resumen', models.CharField(default='Para ver el contenido completo de la noticia, haga click en el boton de abajo.', max_length=250)),
                ('contenido', models.TextField()),
                ('sede', models.CharField(default='Trujillo', max_length=50)),
                ('image', models.ImageField(default='estudiantes.jpg', upload_to='')),
                ('image2', models.ImageField(default='estudiantes.jpg', upload_to='')),
                ('image3', models.ImageField(default='estudiantes.jpg', upload_to='')),
                ('carrera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.carrera')),
            ],
        ),
    ]
