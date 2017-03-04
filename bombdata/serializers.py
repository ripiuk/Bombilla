from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Object, News, Users

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class ObjectSerilizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Object
        fields = ('url', 'number', 'geo_x', 'geo_y', 'filling', 'activity')

class NewsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = News
        fields = ('url', 'number', 'importance', 'text', 'inside_bool', 'geo_x', 'geo_y')

class UsersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Users
        fields = ('url', 'user', 'phone', 'middle_name', 'admin')