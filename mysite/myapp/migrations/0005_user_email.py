# Generated by Django 3.1.7 on 2021-04-18 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_remove_user_first_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.CharField(default='undefined', max_length=100),
        ),
    ]