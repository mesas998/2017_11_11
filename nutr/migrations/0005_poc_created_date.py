# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-07-05 19:37
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('nutr', '0004_auto_20170703_2021'),
    ]

    operations = [
        migrations.AddField(
            model_name='poc',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2017, 7, 5, 19, 37, 30, 725826, tzinfo=utc), verbose_name='date accoount created'),
            preserve_default=False,
        ),
    ]
