# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-10-05 21:34
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('nutr', '0022_auto_20171002_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poc',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2017, 10, 5, 21, 34, 12, 541508, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='poc',
            name='updated_date',
            field=models.DateField(default=datetime.datetime(2017, 10, 5, 21, 34, 12, 541623, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='pocauditlogentry',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2017, 10, 5, 21, 34, 12, 541508, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='pocauditlogentry',
            name='updated_date',
            field=models.DateField(default=datetime.datetime(2017, 10, 5, 21, 34, 12, 541623, tzinfo=utc)),
        ),
    ]
