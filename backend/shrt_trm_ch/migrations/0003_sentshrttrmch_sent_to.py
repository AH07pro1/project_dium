# Generated by Django 4.1.4 on 2023-01-09 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shrt_trm_ch', '0002_receivedshrttrmch_sentshrttrmch_delete_shrttrmch'),
    ]

    operations = [
        migrations.AddField(
            model_name='sentshrttrmch',
            name='sent_to',
            field=models.JSONField(default=list),
        ),
    ]
