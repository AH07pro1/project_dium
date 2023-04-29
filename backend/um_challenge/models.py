from django.db import models


# Create your models here.
class Um_Compete(models.Model):
    SUBJECT_CHOICES = (("Mathematics", "M"), ("History", "H"), ("Ethics", "E"),
                       ("Science", "S"), ("Geography", "G"),
                       ("Languages", "L"), ("Art", "A"),
                       ("Communication/personal_help", "C"), ("Fun", "F"))
    um_compete_challenge_id = models.CharField(max_length=10,
                                               primary_key=True,
                                               default="aabbccddee")
    um_compete_challenge_subject = models.CharField(choices=SUBJECT_CHOICES,
                                                    max_length=40,
                                                    default="Fun")
    host_username = models.CharField(max_length=7, default="aabb11")
    team_1 = models.JSONField(default=list)
    team_2 = models.JSONField(default=list)
    sent_to = models.JSONField(default=list)
    accepted_members = models.JSONField(default=list)
    title = models.CharField(default="Um Compete Title!", max_length=30)
    description = models.TextField(max_length=275)
    questions = models.JSONField(default=list)
    hasStarted = models.BooleanField(default=False)
    team_1_score = models.IntegerField(default=0, null=True)
    team_2_score = models.IntegerField(default=0, null=True)
    finished = models.BooleanField(default=False)
    gamify = models.BooleanField(default=False)
    draft = models.BooleanField(default=False)
