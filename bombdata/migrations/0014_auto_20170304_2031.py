# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-04 20:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bombdata', '0013_auto_20170304_2027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bombdata.UserInfo'),
        ),
    ]