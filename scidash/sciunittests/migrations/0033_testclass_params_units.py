# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-04-15 13:28
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sciunittests', '0032_auto_20190325_2211'),
    ]

    operations = [
        migrations.AddField(
            model_name='testclass',
            name='params_units',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
    ]
