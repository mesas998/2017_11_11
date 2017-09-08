# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-09-03 20:52
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('nutr', '0004_auto_20170812_2053'),
    ]

    operations = [
        migrations.AddField(
            model_name='poc',
            name='updated_date',
            field=models.DateField(default=datetime.datetime(2017, 9, 3, 20, 52, 20, 389587, tzinfo=utc), verbose_name='Date Account Updated'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='poc',
            name='tag',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='nutr.Tag', verbose_name='Country'),
        ),
    ]