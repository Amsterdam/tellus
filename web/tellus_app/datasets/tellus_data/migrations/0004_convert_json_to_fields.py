# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json

from django.db import migrations, models

def convert_json_array(apps, schema_editor):
    TellusData = apps.get_model("tellus_data", "TellusData")

    for row in TellusData.objects.all():
        x = 1
        try:
            for val in json.loads(row.data):
                setattr(row, 'c{}'.format(x), val)
                x += 1
            row.save()
        except AttributeError:
            pass

class Migration(migrations.Migration):

    dependencies = [
        ('tellus_data', '0003_auto_20170206_1040'),
    ]

    operations = [
        migrations.RunSQL("DROP VIEW public.tellus_data_view;"),

        migrations.RunPython(
            convert_json_array,
        ),

        migrations.RemoveField(
            model_name='tellusdata',
            name='data',
        ),
    ]
