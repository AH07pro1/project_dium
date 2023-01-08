from rest_framework import serializers
from .models import ShrtTrmCh

class SendShrtTrmSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShrtTrmCh
        fields = [
            "number_times_sent",
            "challenge_id",
            "title",
            "to_user",
            "due_date",
            "questions",
            "subject",
            "category",
            "description"
        ]

class ReceivedShrtTrmSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShrtTrmCh
        fields = [
            "challenge_id",
            "title",
            "from_user",
            "to_user",
            "due_date",
            "questions",
            "score",
            "score",
            "subject",
            "category",
            "description"
        ]