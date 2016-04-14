# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tank', '0008_room_smoking'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('check_in', models.DateTimeField()),
                ('check_out', models.DateTimeField()),
                ('room_type', models.CharField(max_length=50, choices=[(b'SINGLE', b'single'), (b'DOUBLE', b'double'), (b'TRIPLE', b'triple'), (b'QUAD', b'quad'), (b'QUEEN', b'queen'), (b'KING', b'king'), (b'TWIN', b'twin'), (b'DOUBLE-DOUBLE', b'double-double'), (b'STUDIO', b'studio'), (b'MINI-SUITE', b'mini-suite'), (b'SUITE', b'suite')])),
                ('adults', models.IntegerField(default=1)),
                ('children', models.IntegerField(default=0)),
                ('smoking', models.BooleanField(default=False)),
                ('number_of_rooms', models.IntegerField(default=1)),
                ('confirmed', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='visitor',
            name='check_in',
        ),
        migrations.RemoveField(
            model_name='visitor',
            name='check_out',
        ),
        migrations.AddField(
            model_name='room',
            name='price',
            field=models.DecimalField(default=35.5, max_digits=6, decimal_places=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='visitor',
            name='reservation',
            field=models.ForeignKey(default=None, blank=True, to='tank.Reservation', null=True),
        ),
    ]
