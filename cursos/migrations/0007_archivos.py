# Generated by Django 4.0.5 on 2022-08-09 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0006_alter_comentario_options_remove_cursos_link_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Archivos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Clave')),
                ('titulo', models.CharField(max_length=100)),
                ('descripcion', models.TextField(verbose_name='Descripcion')),
                ('archivo', models.FileField(blank=True, null=True, upload_to='archivos')),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Carga de archivos',
                'ordering': ['create'],
            },
        ),
    ]
