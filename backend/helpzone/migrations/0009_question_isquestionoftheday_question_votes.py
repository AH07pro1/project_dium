# Generated by Django 4.0 on 2023-06-25 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helpzone', '0008_question_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='isQuestionOftheDay',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='question',
            name='votes',
            field=models.IntegerField(default=0),
        ),
    ]
