# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-02-06 13:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sciunittests', '0025_testinstance_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testinstance',
            name='test_suites',
            field=models.ManyToManyField(blank=True, related_name='tests', to='sciunittests.TestSuite'),
        ),
    ]