# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tank', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='visitor',
            field=models.ForeignKey(default=None, blank=True, to='tank.Visitor', null=True),
        ),
    ]
