# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-10-10 21:23
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('nutr', '0026_auto_20171007_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poc',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2017, 10, 10, 21, 23, 31, 528421, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='poc',
            name='updated_date',
            field=models.DateField(default=datetime.datetime(2017, 10, 10, 21, 23, 31, 528540, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='pocauditlogentry',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2017, 10, 10, 21, 23, 31, 528421, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='pocauditlogentry',
            name='updated_date',
            field=models.DateField(default=datetime.datetime(2017, 10, 10, 21, 23, 31, 528540, tzinfo=utc)),
        ),
    ]
