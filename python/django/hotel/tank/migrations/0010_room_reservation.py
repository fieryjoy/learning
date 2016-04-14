# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tank', '0009_auto_20150524_1056'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='reservation',
            field=models.ForeignKey(default=None, blank=True, to='tank.Reservation', null=True),
        ),
    ]
