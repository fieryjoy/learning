# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tank', '0004_auto_20150524_0839'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitor',
            name='title',
            field=models.CharField(default=b'Mr', max_length=20, choices=[(b'Mr', b'Mister'), (b'Mrs', b'Misses'), (b'Miss', b'Miss'), (b'Ms', b'Mizz')]),
        ),
    ]
