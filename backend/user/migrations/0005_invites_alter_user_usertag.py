# Generated by Django 4.1.4 on 2022-12-30 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_remove_user_user_tag_user_usertag'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pending_invites', models.JSONField(default=list)),
                ('accepted_invites', models.JSONField(default=list)),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='usertag',
            field=models.CharField(default='no tags inputed!', max_length=7),
        ),
    ]
