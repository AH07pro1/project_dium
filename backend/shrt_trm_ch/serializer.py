from rest_framework import serializers
from .models import SentShrtTrmCh, ReceivedShrtTrmCh

class SendShrtTrmSerializer(serializers.ModelSerializer):
    class Meta:
        model = SentShrtTrmCh
        fields = "__all__"

class ReceivedShrtTrmSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReceivedShrtTrmCh
        fields = "__all__"