# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-09-25 23:14
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('nutr', '0018_auto_20170924_1951'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='poc',
            options={'get_latest_by': 'modified', 'ordering': ('-modified', '-created')},
        ),
        migrations.AddField(
            model_name='poc',
            name='created',
            field=django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, default=datetime.datetime(2017, 9, 25, 23, 13, 25, 516218, tzinfo=utc), verbose_name='created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='poc',
            name='modified',
            field=django_extensions.db.fields.ModificationDateTimeField(auto_now=True, default=datetime.datetime(2017, 9, 25, 23, 13, 40, 801924, tzinfo=utc), verbose_name='modified'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pocauditlogentry',
            name='created',
            field=django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, default=datetime.datetime(2017, 9, 25, 23, 13, 54, 185243, tzinfo=utc), verbose_name='created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pocauditlogentry',
            name='modified',
            field=django_extensions.db.fields.ModificationDateTimeField(auto_now=True, default=datetime.datetime(2017, 9, 25, 23, 14, 4, 666166, tzinfo=utc), verbose_name='modified'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='poc',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2017, 9, 25, 23, 13, 7, 745862, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='poc',
            name='status',
            field=models.CharField(choices=[('P', 'Prisoner'), ('Q', 'Disappeared'), ('R', 'Released'), ('A', 'Re-arrested'), ('E', 'Executed'), ('D', 'Deceased')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='poc',
            name='updated_date',
            field=models.DateField(default=datetime.datetime(2017, 9, 25, 23, 13, 7, 745966, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='pocauditlogentry',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2017, 9, 25, 23, 13, 7, 745862, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='pocauditlogentry',
            name='status',
            field=models.CharField(choices=[('P', 'Prisoner'), ('Q', 'Disappeared'), ('R', 'Released'), ('A', 'Re-arrested'), ('E', 'Executed'), ('D', 'Deceased')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='pocauditlogentry',
            name='updated_date',
            field=models.DateField(default=datetime.datetime(2017, 9, 25, 23, 13, 7, 745966, tzinfo=utc)),
        ),
    ]
