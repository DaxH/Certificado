# Generated by Django 2.2 on 2020-03-11 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.IntegerField(max_length=10, unique=True)),
                ('nombre', models.CharField(blank=True, max_length=100)),
                ('apellido', models.CharField(blank=True, max_length=100)),
                ('rol', models.CharField(choices=[('1', 'Entidad Receptora'), ('2', 'Entidad Emisora'), ('3', 'Oyente')], max_length=1)),
            ],
        ),
    ]
