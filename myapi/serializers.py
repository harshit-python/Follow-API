from rest_framework import serializers
from . models import User
from . models import Following

class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("user_id", "name")

class Followingserializer(serializers.ModelSerializer):
    class Meta:
        model = Following
        fields = ("seed_user", "followers")