# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-02 06:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_auto_20180502_1202'),
    ]

    operations = [
        migrations.AddField(
            model_name='treatment',
            name='publish',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='treatment',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
