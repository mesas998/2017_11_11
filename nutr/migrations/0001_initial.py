# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-06-20 20:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=63)),
                ('slug', models.SlugField(max_length=63)),
                ('pub_date', models.DateField(verbose_name='date published')),
                ('link', models.URLField(max_length=255)),
            ],
            options={
                'ordering': ['-pub_date'],
                'verbose_name': 'news article',
                'get_latest_by': 'pub_date',
            },
        ),
        migrations.CreateModel(
            name='POC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=63)),
                ('name', models.CharField(max_length=63)),
            ],
        ),
        migrations.AddField(
            model_name='newslink',
            name='poc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nutr.POC'),
        ),
        migrations.AlterUniqueTogether(
            name='newslink',
            unique_together=set([('slug', 'poc')]),
        ),
    ]
