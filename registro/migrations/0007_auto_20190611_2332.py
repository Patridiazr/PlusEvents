# Generated by Django 2.2.1 on 2019-06-12 03:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0006_auto_20190611_2251'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='username',
            new_name='email',
        ),
    ]
