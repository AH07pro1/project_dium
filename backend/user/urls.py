from django.urls import path
from . import views
urlpatterns = [
    path("users/", views.list_user),
    path("users/create", views.create_user),
    path("users/<str:username>", views.detail_user),
    path("users/<str:username>/delete", views.delete_user),
    path("users/<str:username>/update", views.update_user),
    path("users/<str:username>/sent_invites", views.list_sent_invites),
    path("users/<str:username>/sent_invites/create", views.create_sent_invites)
    #pint
]
