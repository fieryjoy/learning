# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tank', '0003_auto_20150524_0809'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='visitor',
        ),
        migrations.AddField(
            model_name='visitor',
            name='room',
            field=models.ForeignKey(default=None, blank=True, to='tank.Room', null=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='reserved',
            field=models.BooleanField(default=False),
        ),
    ]
