# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tank', '0002_auto_20150524_0800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='room_type',
            field=models.CharField(max_length=50, choices=[(b'SINGLE', b'single'), (b'DOUBLE', b'double'), (b'TRIPLE', b'triple'), (b'QUAD', b'quad'), (b'QUEEN', b'queen'), (b'KING', b'king'), (b'TWIN', b'twin'), (b'DOUBLE-DOUBLE', b'double-double'), (b'STUDIO', b'studio'), (b'MINI-SUITE', b'mini-suite'), (b'SUITE', b'suite')]),
        ),
    ]
