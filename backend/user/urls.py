from django.urls import path
from . import views
urlpatterns = [
    path("users/", views.list_user),
    path("users/create", views.create_user),
    path("users/<str:username>", views.detail_user),
    path("users/<str:username>/delete", views.delete_user),
    path("users/<str:username>/update", views.update_user),
<<<<<<< HEAD
    path("users/invites/<str:username>", views.invites)
=======
    path("users/<str:username>/invites", views.invites)
>>>>>>> parent of 63a38f1 (send invites)
]
