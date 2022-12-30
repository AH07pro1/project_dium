from django.db import models
from random import choice
# Create your models here.

nums = [i for i in range(10, 80)]
random_num = choice(nums)

class User(models.Model):

    f_name = models.CharField(max_length=15)
    l_name = models.CharField(max_length=15)
    usertag = models.CharField(max_length=7, default="no tags inputed!")
    level = models.IntegerField(default=1)
    profile_pic = models.URLField(max_length=10000)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=25)
<<<<<<< HEAD
    pending_invites = models.JSONField(default=list)
    accepted_invites = models.JSONField(default=list)
=======
>>>>>>> 0b6873e90160dfef0ff4bf30d0c54d9644666282
    # @property
    # def tag(self) -> str:
    #     tag = self.user_tag + f"${self.f_name[0:2].lower()}{self.l_name[0:2].lower()}{random_num}"
    #     return tag

class Invites(models.Model):
    pending_invites = models.JSONField(default=list)
    accepted_invites = models.JSONField(default=list)