# Generated by Django 4.0 on 2023-04-02 22:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shrt_trm_ch', '0012_alter_sentshrttrmch_mastered'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sentshrttrmch',
            name='mastered',
        ),
    ]
