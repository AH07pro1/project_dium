from django.db import models

# Create your models here.

class SentShrtTrmCh(models.Model):
    SUBJECT_CHOICES = (("Mathematics", "M"), ("History", "H"), ("Ethics", "E"), ("Science", "S"), ("Geography", "G"), ("Languages", "L"), ("Art", "A"), ("Communication/personal_help", "C"))
    challenge_id = models.CharField(blank=False, max_length=11, primary_key=True) #ShTeCha999
    title = models.CharField(default=f"Short Term Challenge", max_length=50)
    from_user = models.CharField(default="aabb11", max_length=7)
    sent_to = models.JSONField(default=list)
    due_date = models.DateField()
    questions = models.JSONField(default=dict)
    subject = models.CharField(choices=SUBJECT_CHOICES,  max_length=40)
    category = models.CharField(default=None, max_length=50)
    description = models.TextField()
    score = models.JSONField(default=["nothing"], null=True, blank=True, unique=False)

class ReceivedShrtTrmCh(models.Model):
    SUBJECT_CHOICES = (("Mathematics", "M"), ("History", "H"), ("Ethics", "E"), ("Science", "S"), ("Geography", "G"), ("Languages", "L"), ("Art", "A"), ("Communication/personal_help", "C"))
    challenge_id = models.CharField(blank=False, max_length=11, primary_key=True)
    title = models.CharField(default=f"Short Term Challenge", max_length=50)
    from_user = models.CharField(default="aabb11", max_length=7)
    due_date = models.DateField()
    questions = models.JSONField(default=dict)
    score = models.IntegerField()
    subject = models.CharField(choices=SUBJECT_CHOICES,  max_length=40)
    category = models.CharField(default=None, max_length=50)
    description = models.TextField()
