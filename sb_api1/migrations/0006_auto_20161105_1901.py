# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-11-05 16:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sb_api1', '0005_auto_20161104_2315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='lastname',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
