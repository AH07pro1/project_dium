# Generated by Django 4.1.4 on 2022-12-26 20:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='challenge',
        ),
        migrations.RemoveField(
            model_name='user',
            name='friend',
        ),
    ]
