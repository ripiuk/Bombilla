"""Bombilla URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from bombdata import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
#router.register(r'groups', views.GroupViewSet)
router.register(r'objects', views.ObjectViewSet)
router.register(r'number', views.NumberViewSet)
router.register(r'news', views.NewsViewSet)
router.register(r'reports', views.ReportViewSet)
router.register(r'user_info', views.UserInfoViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url('^is_auth/', views.ExampleView.as_view()),
    #url(r'^api/v1/numbers/(?P<id>[0-9]+)$', views.number_collection),
]
#urlpatterns = format_suffix_patterns(urlpatterns)
