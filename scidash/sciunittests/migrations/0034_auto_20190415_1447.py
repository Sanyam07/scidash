# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-04-15 14:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sciunittests', '0033_testclass_params_units'),
    ]

    operations = [
        migrations.AddField(
            model_name='scoreinstance',
            name='bool_score',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='scoreinstance',
            name='score',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]
