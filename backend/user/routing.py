from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path("ws/test/<str:challenge_id>/", consumers.ChallengeConsumer.as_asgi()),
]
