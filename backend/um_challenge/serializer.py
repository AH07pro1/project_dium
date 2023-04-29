from rest_framework import serializers
from .models import Um_Compete


class Um_Compete_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Um_Compete
        fields = "__all__"
