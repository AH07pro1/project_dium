from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from .models import User, sentInvites
from .serializer import UserSerializer, SentInvitesSerializer
from django.http import JsonResponse


# Create your views here.



class createUser(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

create_user = createUser.as_view()

class listUser(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]


list_user = listUser.as_view()

class detailUser(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # lookup_field = "pk"
    lookup_field = "usertag"
    lookup_url_kwarg = "username"

    permission_classes = [permissions.IsAuthenticated]

detail_user = detailUser.as_view()

class deleteUser(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "usertag"
    lookup_url_kwarg = "username"
    permission_classes = [permissions.IsAdminUser]

delete_user = deleteUser.as_view()


class updateUser(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "usertag"
    lookup_url_kwarg = "username"
    permission_classes = [permissions.IsAuthenticated]

update_user = updateUser.as_view()

class listsentInvites(generics.ListAPIView):
    queryset = sentInvites.objects.all()
    serializer_class = SentInvitesSerializer
    lookup_field = "usertag"
    lookup_url_kwarg = "username"
    permission_classes = [permissions.IsAuthenticated]

list_sent_invites = listsentInvites.as_view()

class createsentInvites(generics.CreateAPIView):
    queryset = sentInvites.objects.all()
    serializer_class = SentInvitesSerializer
    lookup_field = "usertag"
    lookup_url_kwarg = "username"
    permission_classes = [permissions.IsAuthenticated]

create_sent_invites = createsentInvites.as_view()

