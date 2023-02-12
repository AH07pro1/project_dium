# Generated by Django 4.1.4 on 2023-01-29 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Um_Compete',
            fields=[
                ('um_compete_challenge_id', models.CharField(default='aabbccddee', max_length=10, primary_key=True, serialize=False)),
                ('um_compete_challenge_subject', models.CharField(choices=[('Mathematics', 'M'), ('History', 'H'), ('Ethics', 'E'), ('Science', 'S'), ('Geography', 'G'), ('Languages', 'L'), ('Art', 'A'), ('Communication/personal_help', 'C'), ('Fun', 'F')], default='Fun', max_length=40)),
                ('host_username', models.CharField(default='aabb11', max_length=7)),
                ('team_1', models.JSONField(default=list)),
                ('team_2', models.JSONField(default=list)),
                ('sent_to', models.JSONField(default=list)),
                ('accepted_members', models.JSONField(default=list)),
                ('play_date', models.DateTimeField()),
                ('title', models.CharField(default='Um Compete Title!', max_length=30)),
                ('description', models.TextField(max_length=275)),
                ('questions', models.JSONField(default=list)),
            ],
        ),
    ]