# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-10-07 15:46
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('nutr', '0024_auto_20171007_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poc',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2017, 10, 7, 15, 46, 28, 200555, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='poc',
            name='updated_date',
            field=models.DateField(default=datetime.datetime(2017, 10, 7, 15, 46, 28, 200678, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='pocauditlogentry',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2017, 10, 7, 15, 46, 28, 200555, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='pocauditlogentry',
            name='updated_date',
            field=models.DateField(default=datetime.datetime(2017, 10, 7, 15, 46, 28, 200678, tzinfo=utc)),
        ),
    ]
