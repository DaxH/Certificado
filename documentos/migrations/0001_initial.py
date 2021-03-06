# Generated by Django 2.2 on 2020-03-11 21:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0001_initial'),
        ('carreras', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=150)),
                ('codigo', models.CharField(max_length=10)),
                ('fecha', models.DateField()),
                ('duracion', models.IntegerField()),
                ('carrera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carreras.Carrera')),
                ('usuario', models.ManyToManyField(max_length=10, to='usuarios.Usuario')),
            ],
        ),
    ]
