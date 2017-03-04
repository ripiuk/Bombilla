#from __future__ import unicode_literals
import sys
from django.db import models
from django.contrib.auth.models import User

reload(sys)
sys.setdefaultencoding('utf-8')
# Create your models here.

class Users(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=250)
    middle_name = models.CharField(max_length=250)
    admin = models.BooleanField()

class Number(models.Model):
    number = models.CharField(max_length=250)

class Object(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    number = models.ForeignKey(Number, on_delete=models.CASCADE)
    geo_x = models.FloatField()
    geo_y = models.FloatField()
    filling = models.IntegerField()
    activity = models.BooleanField()

    def __str__(self):
        return self.number

class News(models.Model):
    importance = models.IntegerField()
    text = models.CharField(max_length=500)
    inside_bool = models.BooleanField()
    geo_x = models.IntegerField()
    geo_y = models.IntegerField()

    def __str__(self):
        return str(self.number)

