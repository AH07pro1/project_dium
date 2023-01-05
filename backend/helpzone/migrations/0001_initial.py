# Generated by Django 4.1.4 on 2023-01-05 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answerer', models.CharField(max_length=30)),
                ('answerer_id', models.CharField(max_length=7)),
                ('answered_qn', models.CharField(max_length=7)),
                ('body', models.TextField()),
                ('accepted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_id', models.CharField(max_length=10)),
                ('asked_user', models.CharField(max_length=7)),
                ('title', models.CharField(max_length=140)),
                ('body', models.TextField()),
                ('subject', models.CharField(choices=[('Mathematics', 'M'), ('History', 'H'), ('Ethics', 'E'), ('Science', 'S'), ('Geography', 'G'), ('Languages', 'L'), ('Art', 'A'), ('Communication/personal_help', 'C')], max_length=35)),
                ('category_subject', models.CharField(max_length=15)),
                ('answered', models.BooleanField(default=False)),
                ('answers', models.JSONField(default=list, null=True)),
            ],
        ),
    ]
