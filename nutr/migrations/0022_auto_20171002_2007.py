# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-10-02 20:07
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('nutr', '0021_auto_20170927_2020'),
    ]

    operations = [
        migrations.AddField(
            model_name='poc',
            name='source',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='pocauditlogentry',
            name='source',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='poc',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2017, 10, 2, 20, 7, 52, 390471, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='poc',
            name='updated_date',
            field=models.DateField(default=datetime.datetime(2017, 10, 2, 20, 7, 52, 390716, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='pocauditlogentry',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2017, 10, 2, 20, 7, 52, 390471, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='pocauditlogentry',
            name='updated_date',
            field=models.DateField(default=datetime.datetime(2017, 10, 2, 20, 7, 52, 390716, tzinfo=utc)),
        ),
    ]
