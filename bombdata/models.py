#from __future__ import unicode_literals
import sys
from django.db import models
from django.contrib.auth.models import User

reload(sys)
sys.setdefaultencoding('utf-8')
# Create your models here.

class UserInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_info')
    first_name = models.CharField(max_length=250)
    middle_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    phone = models.CharField(max_length=250)
    admin = models.BooleanField()

    def __str__(self):
        return str(self.user)

class Number(models.Model):
    number = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.number

class Object(models.Model):
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    number = models.ForeignKey(Number, on_delete=models.CASCADE, related_name='objectss')
    geo_x = models.FloatField()
    geo_y = models.FloatField()
    filling = models.IntegerField()
    activity = models.BooleanField()

    def __str__(self):
        return str(self.user) + ' ' + str(self.number)

    '''class Meta:
        unique_together = ('filling', 'activity')
        ordering = ['activity']

    def __unicode__(self):
        return '%d: %s' % (self.filling, self.activity)
'''
class News(models.Model):
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    importance = models.IntegerField()
    text = models.CharField(max_length=500)
    inside_bool = models.BooleanField()
    geo_x = models.FloatField()
    geo_y = models.FloatField()
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver', blank=True, null=True)
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user) + ' ' + str(self.receiver) + ' ' + str(self.date_time)

class Report(models.Model):
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE, related_name='user_infos')
    text = models.CharField(max_length=500)

    def __str__(self):
        return self.text