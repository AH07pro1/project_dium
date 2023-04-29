from rest_framework import generics, permissions
from .models import User, invites, friend, Notification
from .serializer import UserSerializer, InviteSerializer, FriendSerializer, NotificationSerializer
from rest_framework import request
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from .models import Notification, User


class Home(APIView):

    def get(self, request):
        message = {
            "Welcome:":
            "Welcome to DIUM's API\n\n helpzone -> '/helpzone' users -> '/users'  'short_challenges/...'"
        }
        return Response(message)


home = Home.as_view()


# USER branch
class createUser(generics.CreateAPIView):
    """Create a User instance"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


create_user = createUser.as_view()


class listUser(generics.ListAPIView):
    """Display the list of all User instances"""
    queryset = User.objects.all()
    serializer_class = UserSerializer


list_user = listUser.as_view()


class retrieveUser(generics.RetrieveAPIView):
    """Retreive a specific User instance"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "usertag"
    lookup_url_kwarg = "username"


retrieve_user = retrieveUser.as_view()


class deleteUser(generics.DestroyAPIView):
    """Delete a specific User instance"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "usertag"
    lookup_url_kwarg = "username"


delete_user = deleteUser.as_view()


class updateUser(generics.UpdateAPIView):
    """Update a specific User Instance"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "usertag"
    lookup_url_kwarg = "username"


update_user = updateUser.as_view()


# INVITE branch
class listInvites(generics.ListAPIView):
    """List of all invites in the application"""
    queryset = invites.objects.all()
    serializer_class = InviteSerializer


list_of_invites = listInvites.as_view()


class createInvites(generics.CreateAPIView):
    """Create an invite; specify the one who sends the invites, the one who receives it and the invite status"""
    queryset = invites.objects.all()
    serializer_class = InviteSerializer


create_invites = createInvites.as_view()


class updateInvites(generics.UpdateAPIView):
    """Update an invite, more specifically its status attribute"""
    queryset = invites.objects.all()
    serializer_class = InviteSerializer
    lookup_field = "invite_id"
    lookup_url_kwarg = "invite_id"


update_invites = updateInvites.as_view()


class deleteInvites(generics.DestroyAPIView):
    """Delete invite when its status is equivalent to ACCEPTED"""
    queryset = invites.objects.all()
    serializer_class = InviteSerializer
    lookup_field = "invite_id"
    lookup_url_kwarg = "invite_id"


delete_invite = deleteInvites.as_view()


# FRIENDS branch
class listFriends(generics.ListAPIView):
    # queryset = friend.objects.all().filter(my_tag=get_path_var).values()

    def get_queryset(self):
        my_tag = User.objects.get(usertag=self.kwargs["username"])
        print(my_tag.usertag)
        return friend.objects.filter(my_tag=my_tag.usertag)

    serializer_class = FriendSerializer
    lookup_field = "my_tag"

    lookup_url_kwarg = "username"


class deleteFriend(generics.DestroyAPIView):
    """Delete invite when its status is equivalent to ACCEPTED"""
    queryset = friend.objects.all()
    serializer_class = FriendSerializer
    lookup_field = "friend_tag"
    lookup_url_kwarg = "friend_tag"


delete_friend = deleteFriend.as_view()

# class FriendListAPIView(ListAPIView):
# serializer_class = FriendSerializer

#def get_queryset(self):
#user = User.objects.get(usertag=self.kwargs['usertag'])
#return Friend.objects.filter(my_tag=user)

list_friends = listFriends.as_view()


class createFriends(generics.CreateAPIView):
    """If the an invite status is set to ACCEPTED the sent_to user's list of invites will update;
    it will append the from_to user(the one who accepted the invite)."""
    queryset = friend.objects.all()
    serializer_class = FriendSerializer
    lookup_field = "my_tag"
    lookup_url_kwarg = "username"


create_friends = createFriends.as_view()


class NotificationList(generics.ListAPIView):
    """View a specific user's filtered notification objects"""

    queryset = Notification.objects.all()

    serializer_class = NotificationSerializer
    lookup_field = "username"
    lookup_url_kwarg = "username"


user_notification = NotificationList.as_view()


class createNotifications(generics.CreateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer


create_notification = createNotifications.as_view()


class allNotifications(generics.ListAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer


list_notification = allNotifications.as_view()


class deleteNotification(generics.DestroyAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    lookup_field = "id"
    lookup_url_kwarg = "id"


delete_notification = deleteNotification.as_view()