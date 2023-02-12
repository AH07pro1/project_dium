from django.urls import path
from . import views


urlpatterns = [
    path("", views.home),
    path("notifications", views.list_notification),
    path("notifications/create", views.create_notification),
    path("users/", views.list_user),
    path("users/create", views.create_user),
    path("users/<str:username>", views.retrieve_user),
    path("users/<str:username>/delete", views.delete_user),
    path("users/<str:username>/update", views.update_user),
    path("invites", views.list_of_invites),
    path("invites/create", views.create_invites),
    path("invites/<str:invite_id>/delete", views.delete_invite),
    path("invites/<str:invite_id>/update", views.update_invites),
    path("users/<str:username>/friends", views.list_friends),
    path("users/<str:username>/friends/create", views.create_friends),
    path("users/<str:username>/notifications", views.user_notification),

]

