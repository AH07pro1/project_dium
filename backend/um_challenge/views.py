from django.shortcuts import render
from rest_framework import generics
from .models import Um_Compete
from .serializer import Um_Compete_Serializer
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncWebsocketConsumer


# Create your views here.
# all challenges instances
class All_Um_Compete_Challenges(generics.ListAPIView):
    """All challenges instances"""
    queryset = Um_Compete.objects.all()
    serializer_class = Um_Compete_Serializer


all_um_compete_challenges = All_Um_Compete_Challenges.as_view()


class Retreive_Um_Compete_Challenges(generics.RetrieveAPIView):
    """Retreived challenge instance"""
    queryset = Um_Compete.objects.all()
    serializer_class = Um_Compete_Serializer
    lookup_field = "um_compete_challenge_id"
    lookup_url_kwarg = "challenge_id"


retreive_um_compete_challenges = Retreive_Um_Compete_Challenges.as_view()


class Create_Um_Compete_Challenge(generics.CreateAPIView):
    queryset = Um_Compete.objects.all()
    serializer_class = Um_Compete_Serializer


create_um_compete_challenge = Create_Um_Compete_Challenge.as_view()


#update
class Update_Um_Challenge(generics.UpdateAPIView):
    """Update challenge instance"""
    queryset = Um_Compete.objects.all()
    serializer_class = Um_Compete_Serializer
    lookup_field = "um_compete_challenge_id"
    lookup_url_kwarg = "challenge_id"


update_um_challenge = Update_Um_Challenge.as_view()


#delete
class Delete_Um_Challenge(generics.DestroyAPIView):
    """Delete challenge instance"""
    queryset = Um_Compete.objects.all()
    serializer_class = Um_Compete_Serializer
    lookup_field = "um_compete_challenge_id"
    lookup_url_kwarg = "challenge_id"


delete_um_challenge = Delete_Um_Challenge.as_view()
