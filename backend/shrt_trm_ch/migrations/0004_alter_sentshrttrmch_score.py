# Generated by Django 4.1.4 on 2023-01-27 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shrt_trm_ch', '0003_alter_sentshrttrmch_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sentshrttrmch',
            name='score',
            field=models.JSONField(blank=True, default=list, null=True),
        ),
    ]
