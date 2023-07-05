import random
from django.core.management.base import BaseCommand
from helpzone.models import Question

class Command(BaseCommand):
    help = "Used to handle command test"

    def handle(self, *args, **kwargs):
        # Retrieve questions with isQuestionOftheDay set to True and isArchived set to False
        questions = Question.objects.filter(isQuestionOftheDay=True, isArchived=False)
        
   
        # Get the question(s) with the highest votes
        max_votes = max(questions, key=lambda q: q.votes).votes
        top_questions = questions.filter(votes=max_votes)

        # Select a random question if there are multiple top questions, otherwise select the single top question
        question_of_the_day = random.choice(top_questions) if len(top_questions) > 1 else top_questions.first()

        # Delete other questions
        other_questions = questions.exclude(pk=question_of_the_day.pk)
        other_questions.delete()

        # Set isArchived property of question_of_the_day to True
        question_of_the_day.isArchived = True
        question_of_the_day.save()
