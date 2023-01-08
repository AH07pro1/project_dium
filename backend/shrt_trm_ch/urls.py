from django.urls import path, include
from . import views

urlpatterns = [
    path("short_term_challenges/sent_challenges", views.all_sent_challenges),
    path("short_term_challenges/sent_challenges/create", views.create_challenge),
    path("short_term_challenges/received_challenges", views.all_received_challenges),
    path("short_term_challenges/received_challenges/<str:to_user>", views.detail_received_challenges)
]
