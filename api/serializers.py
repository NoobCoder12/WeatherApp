from rest_framework import serializers
from diary.models import Thought
from users.models import CustomUser


class ThoughtSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()

    class Meta:
        model = Thought
        fields = ['id', 'title', 'body', 'slug', 'date', 'banner', 'author']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'city']
