# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-09-19 11:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tellus_data', '0012_add_labels_to_view'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tellusdata',
            options={'ordering': ['id', 'tijd_van', 'tijd_tot', 'richting']},
        ),
    ]
