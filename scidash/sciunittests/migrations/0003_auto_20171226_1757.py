# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-26 17:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sciunittests', '0002_auto_20171226_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testinstance',
            name='build_info',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='testinstance',
            name='hostname',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
    ]
