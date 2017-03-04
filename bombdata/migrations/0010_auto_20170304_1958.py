# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-04 19:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bombdata', '0009_auto_20170304_1930'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='first_name',
            field=models.CharField(default='lol', max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userinfo',
            name='last_name',
            field=models.CharField(default='lol', max_length=250),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='object',
            unique_together=set([('filling', 'activity')]),
        ),
    ]
