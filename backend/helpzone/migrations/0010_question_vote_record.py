# Generated by Django 4.0 on 2023-06-25 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helpzone', '0009_question_isquestionoftheday_question_votes'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='vote_record',
            field=models.JSONField(blank=True, default=list, null=True),
        ),
    ]
