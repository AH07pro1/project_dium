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
    # @property
    # def tag(self) -> str:
    #     tag = self.user_tag + f"${self.f_name[0:2].lower()}{self.l_name[0:2].lower()}{random_num}"
    #     return tag

    # home/users/$adhi76/
    # home/sent_invites -> list of invites
    # home/received_invites


class invites(models.Model):
    choices = [("P", "PENDING"), ("A", "ACCEPTED"), ("D", "DECLINED")]
    sent_to = models.CharField(max_length=7) # User tag
    from_user = models.CharField(max_length=7) # User tag
    invite_status = models.CharField(choices=choices, default=choices[0], max_length=9)


