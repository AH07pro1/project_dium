# Generated by Django 4.0 on 2023-03-30 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shrt_trm_ch', '0004_sentshrttrmch_scores'),
    ]

    operations = [
        migrations.AddField(
            model_name='sentshrttrmch',
            name='cover',
            field=models.JSONField(default={}),
        ),
    ]
