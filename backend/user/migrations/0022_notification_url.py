# Generated by Django 4.0 on 2023-04-05 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0021_notification_notification_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='url',
            field=models.CharField(default='/', max_length=1000),
        ),
    ]
