# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-23 11:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sciunittests', '0005_auto_20180118_1516'),
    ]

    operations = [
        migrations.AddField(
            model_name='score',
            name='raw',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='score',
            name='summary',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
    ]
