# Generated by Django 2.2 on 2020-03-12 04:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_auto_20200311_2013'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='decula',
            new_name='cedula',
        ),
    ]
