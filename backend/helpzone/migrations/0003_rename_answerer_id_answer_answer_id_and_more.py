
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('helpzone', '0002_remove_answer_id_remove_question_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='answerer_id',
            new_name='answer_id',
        ),
        migrations.RenameField(
            model_name='answer',
            old_name='answered_qn',
            new_name='answered_qn_id',
        ),
    ]
