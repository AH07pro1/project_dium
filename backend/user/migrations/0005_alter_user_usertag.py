# Generated by Django 4.1.4 on 2022-12-30 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_remove_user_user_tag_user_usertag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='usertag',
            field=models.CharField(default='no tags inputed!', max_length=7),
        ),
    ]
