from django.db import models

class User(models.Model):
    f_name = models.CharField(max_length=15)
    l_name = models.CharField(max_length=15)
    usertag = models.CharField(max_length=7, default="aabb11", null=False)
    level = models.IntegerField(default=1)
    profile_pic = models.URLField(max_length=10000)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=25)


class invites(models.Model):
    invite_id = models.CharField(max_length=8, primary_key=True)
    choices = [("P", "PENDING"), ("A", "ACCEPTED"), ("D", "DECLINED")]
    sent_to = models.CharField(max_length=7) 
    from_user = models.CharField(max_length=7) 
    invite_status = models.CharField(choices=choices, default=choices[0], max_length=9)


# USE Foreign KEYS
class friend(models.Model):
    # fk = models.ForeignKey(User, on_delete=models.CASCADE, db_constraint=False)
    my_tag = models.CharField(max_length=7, default="aabb11")
    friend_tag = models.CharField(max_length=7, primary_key=True)
    # @property
    # def my_tag(self):
    #     return self.fk.usertag

class Notifications(models.Model):
    targeted_user = models.CharField(max_length=7, default="aabb11", primary_key=True)
    message = models.CharField(max_length=100, default="notification")
    received = models.BooleanField(default=False)
