from django.db import models

# Create your models here.
# category


# question
class Question(models.Model):
    SUBJECT_CHOICES = (("Mathematics", "M"), ("History", "H"), ("Ethics", "E"), ("Science", "S"), ("Geography", "G"), ("Languages", "L"), ("Art", "A"), ("Communication/personal_help", "C"))
    question_id = models.CharField(max_length=10, primary_key=True) # artpo78989
    asked_user = models.CharField(max_length=7) #aabb11
    title = models.CharField(max_length=140, blank=False)
    body = models.TextField(blank=False) # ______________________
    subject = models.CharField(choices=SUBJECT_CHOICES, max_length=35) # Science
    category_subject = models.CharField(max_length=15) # litterature, algebra
    answered = models.BooleanField(default=False)
    answers = models.JSONField(default=dict, null=True, blank=True)


# answer
class Answer(models.Model):
    answerer = models.CharField(max_length=30)
    answer_id = models.CharField(max_length=7, primary_key=True) # aabb11
    answered_qn_id = models.CharField(max_length=7) # artpo78989(question id)
    body = models.TextField()
    accepted = models.BooleanField(default=False)

