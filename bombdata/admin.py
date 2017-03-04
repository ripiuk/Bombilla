from django.contrib import admin
from .models import Object, News, Number, Report, UserInfo

# Register your models here.
admin.site.register(Object)
admin.site.register(News)
admin.site.register(Number)
admin.site.register(Report)
admin.site.register(UserInfo)
