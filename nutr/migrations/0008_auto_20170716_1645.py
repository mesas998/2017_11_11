# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-07-16 16:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nutr', '0007_auto_20170711_1915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poc',
            name='created_date',
            field=models.DateField(verbose_name='Date Account Created'),
        ),
    ]