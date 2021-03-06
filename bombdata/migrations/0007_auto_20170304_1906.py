# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-04 19:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bombdata', '0006_userinfo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='object',
            options={'ordering': ['activity']},
        ),
        migrations.AlterField(
            model_name='object',
            name='number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='numbers', to='bombdata.Number'),
        ),
        migrations.AlterUniqueTogether(
            name='object',
            unique_together=set([('number', 'activity')]),
        ),
    ]
