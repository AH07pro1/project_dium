from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from .models import User, invites, friend
from .serializer import UserSerializer, InviteSerializer, FriendSerializer
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


class listInvites(generics.ListAPIView):
    queryset = invites.objects.all()
    serializer_class = InviteSerializer
    permission_classes = [permissions.IsAdminUser]

list_of_invites = listInvites.as_view()

class createInvites(generics.CreateAPIView):
    queryset = invites.objects.all()
    serializer_class = InviteSerializer
    permission_classes = [permissions.IsAuthenticated]

create_invites = createInvites.as_view()


class updateInvites(generics.UpdateAPIView):
    queryset = invites.objects.all()
    serializer_class = InviteSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = "sent_to"
    lookup_url_kwarg = "inviter"

update_invites = updateInvites.as_view()


class listFriends(generics.ListAPIView):
    queryset = friend.objects.all()
    serializer_class = FriendSerializer   # home/users/$rahi76/friends
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = "my_tag"
    lookup_url_kwarg = "username"

list_friends = listFriends.as_view()

class createFriends(generics.CreateAPIView):
    queryset = friend.objects.all()
    serializer_class = FriendSerializer   # home/users/$rahi76/friends
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = "my_tag"
    lookup_url_kwarg = "username"

create_friends = createFriends.as_view()