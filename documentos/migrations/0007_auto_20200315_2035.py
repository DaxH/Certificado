# Generated by Django 2.2 on 2020-03-16 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documentos', '0006_auto_20200312_1247'),
    ]

    operations = [
        migrations.CreateModel(
            name='EntidadEmisora',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institucion', models.CharField(blank=True, max_length=100)),
                ('representante', models.CharField(blank=True, max_length=100)),
                ('logo', models.ImageField(upload_to='static/imagenes')),
            ],
        ),
        migrations.CreateModel(
            name='EntidadReceptora',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institucion', models.CharField(blank=True, max_length=100)),
                ('representante', models.CharField(blank=True, max_length=100)),
                ('logo', models.ImageField(upload_to='static/imagenes')),
            ],
        ),
        migrations.RemoveField(
            model_name='documento',
            name='entidad',
        ),
        migrations.DeleteModel(
            name='Entidad',
        ),
        migrations.AddField(
            model_name='documento',
            name='entidad_emisora',
            field=models.ManyToManyField(null=True, to='documentos.EntidadEmisora'),
        ),
        migrations.AddField(
            model_name='documento',
            name='entidad_receptora',
            field=models.ManyToManyField(null=True, to='documentos.EntidadReceptora'),
        ),
    ]