# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-08-08 16:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('nutr', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=63)),
                ('slug', models.SlugField(help_text='A label for URL config', max_length=63, unique_for_month='pub_date')),
                ('text', models.TextField()),
                ('pub_date', models.DateField(auto_now_add=True, verbose_name='date published')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to=settings.AUTH_USER_MODEL)),
                ('pocs', models.ManyToManyField(blank=True, related_name='blog_posts', to='nutr.POC')),
                ('tags', models.ManyToManyField(blank=True, related_name='blog_posts', to='nutr.Tag')),
            ],
            options={
                'ordering': ['-pub_date', 'title'],
                'permissions': (('view_future_post', 'Can view unpublished Post'),),
                'verbose_name': 'blog post',
                'get_latest_by': 'pub_date',
            },
        ),
    ]
