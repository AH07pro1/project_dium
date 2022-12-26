from django.shortcuts import render
from rest_framework import generics
from .models import User
from .serializer import UserSerializer

# Create your views here.
class createUser(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

create_user = createUser.as_view()