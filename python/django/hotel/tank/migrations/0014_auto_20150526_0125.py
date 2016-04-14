# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.core.management import call_command

fixture = 'initial_data_for_migrations'

def load_fixture(apps, schema_editor):
    call_command('loaddata', fixture, app_label='tank') 


def unload_fixture(apps, schema_editor):
    "Brutally deleting all entries for this model..."

    MyModel = apps.get_model("tank", "ModelName")
    MyModel.objects.all().delete()

class Migration(migrations.Migration):

    dependencies = [
        ('tank', '0013_auto_20150525_2107'),
    ]

    operations = [
        migrations.RunPython(load_fixture, reverse_code=unload_fixture),
    ]
