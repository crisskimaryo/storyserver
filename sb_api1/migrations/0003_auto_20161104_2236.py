# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-11-04 19:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sb_api1', '0002_booksmodel_cover'),
    ]

    operations = [
        migrations.AddField(
            model_name='booksmodel',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sb_api1.author'),
        ),
        migrations.AddField(
            model_name='booksmodel',
            name='content',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sb_api1.contents'),
        ),
        migrations.AlterField(
            model_name='booksmodel',
            name='cover',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='booksmodel',
            name='extra',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
