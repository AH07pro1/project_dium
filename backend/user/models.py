from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.


class User(models.Model):
    f_name = models.CharField(max_length=10, blank=False)
    l_name = models.CharField(max_length=10, blank=False)
    profile_pic = models.URLField()
    email = models.EmailField(max_length=50, blank=False)
    password = models.CharField(max_length=15, blank=False)