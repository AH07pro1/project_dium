from django.urls import path
from . import views

urlpatterns = [
    path("um_compete_challenges/all_challenges",
         views.all_um_compete_challenges),
    path("um_compete_challenges/all_challenges/<str:challenge_id>",
         views.retreive_um_compete_challenges),
    path("um_compete_challenges/all_challenges/<str:challenge_id>/update",
         views.update_um_challenge),
    path("um_compete_challenges/all_challenges/<str:challenge_id>/delete",
         views.delete_um_challene),
    path("um_compete_challenges/create", views.create_um_compete_challenge),
]