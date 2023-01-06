# Generated by Django 4.1.4 on 2023-01-06 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0014_notifications'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notifications',
            name='id',
        ),
        migrations.AddField(
            model_name='notifications',
            name='received',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='notifications',
            name='targeted_user',
            field=models.CharField(default='aabb11', max_length=7, primary_key=True, serialize=False),
        ),
    ]
