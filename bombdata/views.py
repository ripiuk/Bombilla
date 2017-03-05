from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, generics
from .models import Object, News, Number, Report, UserInfo
from .serializers import UserSerializer, ObjectSerilizer, NewsSerializer, NumberSerializer, ReportSerializer, UserInfoSerializer
#from django.http import request
#import django_filters
#from django_filters.rest_framework import DjangoFilterBackend

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


"""class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
"""

class ObjectViewSet(viewsets.ModelViewSet):
    #premission_classes = (IsAuthenticated, )
    queryset = Object.objects.all()
    serializer_class = ObjectSerilizer
    #filter_beckends = (DjangoFilterBackend,)
    #filter_fields = ('object', 'object__filling',)
    """def get_queryset(self):

        queryset = Object.objects.all()
        submission = self.request.query_params.get('filling', None)
        if submission is not None:
            queryset = queryset.filter(filling=filling)

        return queryset"""

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


class ObjectList(generics.ListCreateAPIView):
    serializer_class = ObjectSerilizer


    def get_queryset(self):
        filling = self.request.GET.get('filling', None)
        if filling:
            return Object.objects.all().filter(filling=filling)
        else:
            return Object.objects.all()

class ObjectList(generics.ListAPIView):
    queryset = Object.objects.all()
    serializer_class = ObjectSerilizer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_fields=('filling',)

    """def get_queryset(self):
        #queryset = super(ObjectList, self).get_queryset()
        #return queryset.filter(object__pk=self.kwargs.get('pk'))
        pk = request.GET.get('filling')
        return Object.objects.filter(filling=filling)"""

    def get_queryset(self):
        return Object.objects.filter(filling=self.kwargs['filling'])