# Generated by Django 4.1.4 on 2023-01-08 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShrtTrmCh',
            fields=[
                ('number_times_sent', models.IntegerField(default=1)),
                ('challenge_id', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('title', models.CharField(default='Short Term Challenge<django.db.models.fields.IntegerField>', max_length=50)),
                ('from_user', models.CharField(default='aabb11', max_length=7)),
                ('to_user', models.CharField(default='bbbb22', max_length=7)),
                ('due_date', models.DateField(auto_now=True)),
                ('questions', models.JSONField(default=dict)),
                ('score', models.IntegerField(default=0)),
                ('subject', models.CharField(choices=[('Mathematics', 'M'), ('History', 'H'), ('Ethics', 'E'), ('Science', 'S'), ('Geography', 'G'), ('Languages', 'L'), ('Art', 'A'), ('Communication/personal_help', 'C')], max_length=40)),
                ('category', models.CharField(default=None, max_length=50)),
                ('description', models.TextField()),
            ],
        ),
    ]