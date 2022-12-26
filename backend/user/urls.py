from django.urls import path
from .views import create_user
urlpatterns = [
    path("user/", create_user)
]
