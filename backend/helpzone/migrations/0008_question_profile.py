# Generated by Django 4.0 on 2023-04-12 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helpzone', '0007_alter_question_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='profile',
            field=models.URLField(default=''),
        ),
    ]
