# Generated by Django 2.2 on 2020-03-12 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documentos', '0005_auto_20200311_2126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entidad',
            name='logo',
            field=models.ImageField(upload_to='static/imagenes'),
        ),
    ]