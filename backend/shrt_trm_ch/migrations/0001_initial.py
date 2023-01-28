# Generated by Django 4.1.4 on 2023-01-23 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ReceivedShrtTrmCh',
            fields=[
                ('challenge_id', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('title', models.CharField(default='Short Term Challenge', max_length=50)),
                ('from_user', models.CharField(default='aabb11', max_length=7)),
                ('due_date', models.DateField()),
                ('questions', models.JSONField(default=dict)),
                ('score', models.IntegerField()),
                ('subject', models.CharField(choices=[('Mathematics', 'M'), ('History', 'H'), ('Ethics', 'E'), ('Science', 'S'), ('Geography', 'G'), ('Languages', 'L'), ('Art', 'A'), ('Communication/personal_help', 'C')], max_length=40)),
                ('category', models.CharField(default=None, max_length=50)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SentShrtTrmCh',
            fields=[
                ('challenge_id', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('title', models.CharField(default='Short Term Challenge', max_length=50)),
                ('from_user', models.CharField(default='aabb11', max_length=7)),
                ('sent_to', models.JSONField(default=list)),
                ('due_date', models.DateField()),
                ('questions', models.JSONField(default=dict)),
                ('subject', models.CharField(choices=[('Mathematics', 'M'), ('History', 'H'), ('Ethics', 'E'), ('Science', 'S'), ('Geography', 'G'), ('Languages', 'L'), ('Art', 'A'), ('Communication/personal_help', 'C')], max_length=40)),
                ('category', models.CharField(default=None, max_length=50)),
                ('description', models.TextField()),
            ],
        ),
    ]
