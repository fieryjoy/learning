# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tank', '0007_auto_20150524_0905'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='smoking',
            field=models.BooleanField(default=False),
        ),
    ]
