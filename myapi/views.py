from django.shortcuts import render
from rest_framework import viewsets
from . serializers import Userserializer
from . models import User
from . serializers import Followingserializer
from . models import Following


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("id")
    serializer_class = Userserializer


class FollowingViewSet(viewsets.ModelViewSet):
    serializer_class = Followingserializer
    queryset = Following.objects.all()