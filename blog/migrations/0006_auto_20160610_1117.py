# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-10 11:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20160610_1113'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='name',
        ),
        migrations.AddField(
            model_name='category',
            name='title',
            field=models.CharField(default='없음', max_length=100),
        ),
    ]