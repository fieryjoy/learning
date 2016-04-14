# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tank', '0011_auto_20150524_1541'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoomReservation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='visitor',
            name='reservation',
        ),
        migrations.RemoveField(
            model_name='visitor',
            name='room',
        ),
        migrations.AddField(
            model_name='reservation',
            name='visitor',
            field=models.ForeignKey(default=None, blank=True, to='tank.Visitor', null=True),
        ),
        migrations.RemoveField(
            model_name='room',
            name='reservation',
        ),
        migrations.AddField(
            model_name='roomreservation',
            name='reservation',
            field=models.ForeignKey(to='tank.Reservation'),
        ),
        migrations.AddField(
            model_name='roomreservation',
            name='room',
            field=models.ForeignKey(to='tank.Room'),
        ),
        migrations.AddField(
            model_name='room',
            name='reservation',
            field=models.ManyToManyField(to='tank.Reservation', through='tank.RoomReservation'),
        ),
    ]
