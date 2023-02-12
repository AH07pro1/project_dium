from django.urls import path, include
from . import views

urlpatterns = [
    path("short_challenges/all_sent_challenges", views.all_sent_challenges),
    path("short_challenges/create", views.create_sent_challenges),
    path("short_challenges/all_sent_challenges/<str:challenge_id>", views.detail_sent_challenge),
    path("short_challenges/all_received_challenges", views.all_received_challenges),
    path("short_challenges/all_received_challenges/create", views.create_received_challenges),
    path("short_challenges/all_received_challenges/<str:challenge_id>", views.detail_received_challenge),
    path("short_challenges/all_sent_challenges/<str:challenge_id>/update", views.update_sent_shrt_ch)
]
