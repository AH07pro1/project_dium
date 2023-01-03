from rest_framework import serializers
from .models import User, invites, friend

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "f_name",
            "l_name",
            "profile_pic",
            "email",
            "password",
            'usertag',
            'level',
        ]

class InviteSerializer(serializers.ModelSerializer):
    class Meta:
        model = invites
        fields = "__all__"

class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = friend
        fields = [
            "my_tag",
            "friend_tag"
        ]

