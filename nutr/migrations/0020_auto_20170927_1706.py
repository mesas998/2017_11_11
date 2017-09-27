# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-09-27 17:06
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('nutr', '0019_auto_20170925_2314'),
    ]

    operations = [
        migrations.AddField(
            model_name='poc',
            name='arrested_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='poc',
            name='charge',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='pocauditlogentry',
            name='arrested_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pocauditlogentry',
            name='charge',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='poc',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2017, 9, 27, 17, 6, 21, 877183, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='poc',
            name='updated_date',
            field=models.DateField(default=datetime.datetime(2017, 9, 27, 17, 6, 21, 877287, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='pocauditlogentry',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2017, 9, 27, 17, 6, 21, 877183, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='pocauditlogentry',
            name='updated_date',
            field=models.DateField(default=datetime.datetime(2017, 9, 27, 17, 6, 21, 877287, tzinfo=utc)),
        ),
    ]
