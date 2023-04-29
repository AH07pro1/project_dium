from rest_framework import serializers
from .models import User, invites, friend, Notification


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            "f_name", "l_name", "profile_pic", "email", "password", 'usertag',
            'level', "xp"
        ]


class InviteSerializer(serializers.ModelSerializer):

    class Meta:
        model = invites
        fields = "__all__"


class FriendSerializer(serializers.ModelSerializer):

    class Meta:
        model = friend
        fields = ["my_tag", "friend_tag"]


class NotificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notification
        fields = "__all__"
