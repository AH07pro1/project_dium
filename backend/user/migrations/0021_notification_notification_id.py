# Generated by Django 4.0 on 2023-03-04 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0020_user_xp'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='notification_id',
            field=models.IntegerField(default=0),
        ),
    ]
