# Generated by Django 4.0 on 2023-03-01 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user',
         '0019_remove_notification_timestamp_notification_from_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='User',
            name='xp',
            field=models.IntegerField(default=0),
        ),
    ]
