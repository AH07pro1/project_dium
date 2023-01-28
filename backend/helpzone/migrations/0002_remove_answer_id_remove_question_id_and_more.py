
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helpzone', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='id',
        ),
        migrations.RemoveField(
            model_name='question',
            name='id',
        ),
        migrations.AlterField(
            model_name='answer',
            name='answerer_id',
            field=models.CharField(max_length=7, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='question',
            name='answers',
            field=models.JSONField(blank=True, default=dict, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_id',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]
