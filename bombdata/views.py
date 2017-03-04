from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, generics
from .models import Object, News, Number, Report, UserInfo
from .serializers import UserSerializer, ObjectSerilizer, NewsSerializer, NumberSerializer, ReportSerializer, UserInfoSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


"""class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
"""

class ObjectViewSet(viewsets.ModelViewSet):
    queryset = Object.objects.all()
    serializer_class = ObjectSerilizer

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

class NumberViewSet(viewsets.ModelViewSet):
    queryset = Number.objects.all()
    serializer_class = NumberSerializer

class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

class UserInfoViewSet(viewsets.ModelViewSet):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer

class ObjectList(generics.ListAPIView):
    serializer_class = ObjectSerilizer

    def get_queryset(self):
        number = self.request.number
        return Object.objects.filter(number=number)