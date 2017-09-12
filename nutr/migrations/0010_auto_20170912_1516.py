# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-09-12 15:16
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('nutr', '0009_auto_20170912_1516'),
    ]

    operations = [
        migrations.AddField(
            model_name='poc',
            name='arrest_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='poc',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2017, 9, 12, 15, 16, 58, 756471, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='poc',
            name='updated_date',
            field=models.DateField(default=datetime.datetime(2017, 9, 12, 15, 16, 58, 756572, tzinfo=utc)),
        ),
    ]
