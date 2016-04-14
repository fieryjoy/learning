# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tank', '0005_visitor_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='floor_number',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='room',
            name='number',
            field=models.IntegerField(default=0),
        ),
    ]
