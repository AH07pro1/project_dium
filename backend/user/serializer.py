from rest_framework import serializers
from .models import User, Invites

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
        model = Invites 
        fields = "__all__"



#add friends later