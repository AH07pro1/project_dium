# Generated by Django 4.1.4 on 2023-02-01 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('um_challenge', '0003_remove_um_compete_play_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='um_compete',
            name='hasStarted',
            field=models.BooleanField(default=False),
        ),
    ]