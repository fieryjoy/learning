# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tank', '0012_auto_20150524_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitor',
            name='email',
            field=models.EmailField(unique=True, max_length=254),
        ),
    ]
