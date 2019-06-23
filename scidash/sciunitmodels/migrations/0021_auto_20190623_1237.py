# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-06-23 12:37
from __future__ import unicode_literals

from django.db import migrations
from scidash.sciunitmodels.models import ModelClass


def populate_classes(apps, schema_editor):
    data = [
        {
            'class_name': 'ReducedModel',
            'url': None,
            'import_path': 'neuronunit.models.reduced.ReducedModel'
        },
        {
            'class_name': 'VeryReducedModel',
            'url': None,
            'import_path': 'neuronunit.models.reduced.VeryReducedModel'
        },
        {
            'class_name': 'ChannelModel',
            'url': None,
            'import_path': 'neuronunit.models.channel.ChannelModel'
        },
        {
            'class_name': 'LEMSModel',
            'url': None,
            'import_path': 'neuronunit.models.lems.LEMSModel'
        },
        {
            'class_name': 'SwcCellModel',
            'url': None,
            'import_path': 'neuronunit.models.morphology.SwcCellModel'
        },
        {
            'class_name': 'SincleCellModel',
            'url': None,
            'import_path': 'neuronunit.models.section_extension.SingleCellModel'
        },
        {
            'class_name': 'StaticModel',
            'url': None,
            'import_path': 'neuronunit.models.static.StaticModel'
        },
        {
            'class_name': 'VeryReducedModel',
            'url': None,
            'import_path': 'neuronunit.models.very_reduced.VeryReducedModel'
        },
    ]

    for model in data:
        obj, created = ModelClass.objects.get_or_create(
            **model
        )


class Migration(migrations.Migration):

    dependencies = [
        ('sciunitmodels', '0020_auto_20190510_1306'),
    ]

    operations = [
        migrations.RunPython(populate_classes)
    ]
