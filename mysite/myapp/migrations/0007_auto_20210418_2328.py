# Generated by Django 3.1.7 on 2021-04-18 23:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20210418_2324'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='first_name',
            new_name='firstName',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='last_name',
            new_name='lastName',
        ),
    ]
