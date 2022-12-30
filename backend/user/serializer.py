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
<<<<<<< HEAD
            'pending_invites',
            'accepted_invites'
=======
>>>>>>> 0b6873e90160dfef0ff4bf30d0c54d9644666282
        ]

class InviteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invites 
        fields = "__all__"



#add friends later