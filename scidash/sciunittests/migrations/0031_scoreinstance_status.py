# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-03-25 17:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sciunittests', '0030_testclass_units'),
    ]

    operations = [
        migrations.AddField(
            model_name='scoreinstance',
            name='status',
            field=models.CharField(choices=[('s', 'Scheduled'), ('c', 'Calculated')], default='c', max_length=3),
        ),
    ]
