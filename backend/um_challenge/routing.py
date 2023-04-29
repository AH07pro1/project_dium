from django.urls import path
from . import consumers
from user.consumers import NotificationConsumer

websocket_urlpatterns = [
    path("ws/test/<str:challenge_id>/", consumers.ChallengeConsumer.as_asgi()),
    path('ws/notifications/<str:usertag>/', NotificationConsumer.as_asgi()),
]
