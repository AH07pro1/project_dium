from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.


class User(models.Model):
    f_name = models.CharField(max_length=15)
    l_name = models.CharField(max_length=15)
    profile_pic = models.URLField(max_length=10000)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=25)