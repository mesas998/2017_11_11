# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-11-05 22:38
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('nutr', '0029_auto_20171105_2141'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poc',
            name='changed_by',
        ),
        migrations.RemoveField(
            model_name='pocauditlogentry',
            name='changed_by',
        ),
        migrations.AlterField(
            model_name='poc',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2017, 11, 5, 22, 38, 1, 415809, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='poc',
            name='updated_date',
            field=models.DateField(default=datetime.datetime(2017, 11, 5, 22, 38, 1, 415914, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='pocauditlogentry',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2017, 11, 5, 22, 38, 1, 415809, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='pocauditlogentry',
            name='updated_date',
            field=models.DateField(default=datetime.datetime(2017, 11, 5, 22, 38, 1, 415914, tzinfo=utc)),
        ),
    ]
