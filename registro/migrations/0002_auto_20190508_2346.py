# Generated by Django 2.2.1 on 2019-05-09 03:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='contrasenia',
            new_name='password',
        ),
    ]