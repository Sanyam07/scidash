# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-10 14:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sciunitmodels', '0005_modelinstance_backend'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelinstance',
            name='hash_id',
            field=models.CharField(default='legacy_hashid', max_length=100),
            preserve_default=False,
        ),
    ]
