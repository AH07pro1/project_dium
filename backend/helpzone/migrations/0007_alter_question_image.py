# Generated by Django 4.0 on 2023-02-26 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helpzone', '0006_alter_question_answers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]