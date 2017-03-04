# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-04 20:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bombdata', '0010_auto_20170304_1958'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='object',
            options={},
        ),
        migrations.AlterField(
            model_name='object',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_infos', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_info', to=settings.AUTH_USER_MODEL, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='object',
            unique_together=set([]),
        ),
    ]
