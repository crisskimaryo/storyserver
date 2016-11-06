# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-11-04 19:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100, null=True)),
                ('lastname', models.TextField(null=True)),
                ('email', models.CharField(max_length=100, null=True)),
                ('phone', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='booksmodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
                ('extra', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='contents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_title', models.CharField(max_length=100, null=True)),
                ('content', models.TextField(null=True)),
                ('chapter', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]