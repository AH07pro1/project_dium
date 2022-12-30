from django.db import models
from django.contrib.postgres.fields import ArrayField
from random import choice
# Create your models here.

nums = [i for i in range(10, 80)]
random_num = choice(nums)

class User(models.Model):

    f_name = models.CharField(max_length=15)
    l_name = models.CharField(max_length=15)
    usertag = models.CharField(max_length=6, default=" ")
    level = models.IntegerField(default=1)
    profile_pic = models.URLField(max_length=10000)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=25)
    # pending_friends = ArrayField(models.CharField(max_length=7, default="$%$%$%"), blank=True, default=list)
    # accepted_friends = ArrayField(models.CharField(max_length=7, default="$%$%$%"), blank=True, default=list)
    # pending_friends = models.JSONField()
    # accepted_friends = models.JSONField()
    # @property
    # def tag(self) -> str:
    #     tag = self.user_tag + f"${self.f_name[0:2].lower()}{self.l_name[0:2].lower()}{random_num}"
    #     return tag