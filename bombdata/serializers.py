from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Object, News, Number, Report, UserInfo



"""class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'id', 'name')
"""

class NewsSerializer(serializers.ModelSerializer):
    user_first_name = serializers.CharField(read_only=True, source='user.first_name')
    user_middle_name = serializers.CharField(read_only=True, source='user.middle_name')
    user_last_name = serializers.CharField(read_only=True, source='user.last_name')
    user_phone = serializers.CharField(read_only=True, source='user.phone')
    user_admin = serializers.BooleanField(read_only=True, source='user.admin')
    class Meta:
        model = News
        fields = ('url', 'id', 'user', 'user_first_name', 'user_middle_name', 'user_last_name', 'user_phone', 'user_admin', 'importance', 'text', 'inside_bool', 'geo_x', 'geo_y', 'receiver', 'date_time')



class UserInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserInfo
        fields = ('url', 'id', 'user', 'first_name', 'middle_name', 'last_name', 'phone', 'admin')

class UserSerializer(serializers.ModelSerializer):
    user_info = UserInfoSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'email', 'user_info')

class ObjectSerilizer(serializers.ModelSerializer):
    #numbers = NumberSerializer(many=True, read_only=True)
    number_info = serializers.CharField(read_only=True, source = 'number.number')
    user_first_name = serializers.CharField(read_only=True, source = 'user.first_name')
    user_middle_name = serializers.CharField(read_only=True, source='user.middle_name')
    user_last_name = serializers.CharField(read_only=True, source='user.last_name')
    user_phone = serializers.CharField(read_only=True, source='user.phone')
    user_admin = serializers.BooleanField(read_only=True, source='user.admin')
    class Meta:
        model = Object
        fields = ('url', 'id', 'user', 'user_first_name', 'user_middle_name', 'user_last_name', 'user_phone', 'user_admin', 'number', 'number_info', 'geo_x', 'geo_y', 'filling', 'activity')


class NumberSerializer(serializers.ModelSerializer):
    objectss = ObjectSerilizer(many =True, read_only=True)
    class Meta:
        model = Number
        fields = ('url', 'id', 'number', 'objectss')

class ReportSerializer(serializers.ModelSerializer):
    user_first_name = serializers.CharField(read_only=True, source='user.first_name')
    user_middle_name = serializers.CharField(read_only=True, source='user.middle_name')
    user_last_name = serializers.CharField(read_only=True, source='user.last_name')
    user_phone = serializers.CharField(read_only=True, source='user.phone')
    user_admin = serializers.BooleanField(read_only=True, source='user.admin')
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    user_infos = UserInfoSerializer(many =True, read_only=True)
    class Meta:
        model = Report
        fields = ('user', 'user_infos',  'url', 'id', 'user', 'user_first_name', 'user_middle_name', 'user_last_name', 'user_phone', 'user_admin', 'text')