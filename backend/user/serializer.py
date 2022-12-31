from rest_framework import serializers
from .models import User, sentInvites

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

class SentInvitesSerializer(serializers.ModelSerializer):
    class Meta:
        model = sentInvites
        fields = "__all__"