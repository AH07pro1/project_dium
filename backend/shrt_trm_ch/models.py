from django.db import models

# Create your models here.

class ShrtTrmCh(models.Model):
    SUBJECT_CHOICES = (("Mathematics", "M"), ("History", "H"), ("Ethics", "E"), ("Science", "S"), ("Geography", "G"), ("Languages", "L"), ("Art", "A"), ("Communication/personal_help", "C"))
    number_times_sent = models.IntegerField(default=1)
    challenge_id = models.CharField(blank=False, max_length=11, primary_key=True) #ShTeCha999
    title = models.CharField(default=f"Short Term Challenge{number_times_sent}", max_length=50)
    from_user = models.CharField(default="aabb11", max_length=7)
    to_user = models.CharField(default="bbbb22", max_length=7)
    due_date = models.DateField()
    questions = models.JSONField(default=dict)
    score = models.IntegerField(default=0)
    subject = models.CharField(choices=SUBJECT_CHOICES,  max_length=40)
    category = models.CharField(default=None, max_length=50)
    description = models.TextField()


# -number_of_time_sent
# - short_term_id = 
# - title = Random Title
# - from_user= $adhi70
# - to_user=[$rahi76]
# - due_date= 2023/01/08
# - questions={question:[answer, type, weighting(pondération)]}
# - score = 100%
# - subject = Math
# - category = Arithmetics 
# - description(purpose) = ".............."
