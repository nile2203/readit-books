# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-26 19:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('author', models.CharField(max_length=70)),
                ('review', models.TextField(blank=True, max_length=500, null=True)),
                ('date_reviewed', models.DateTimeField(blank=True, default=None, null=True)),
                ('is_favourite', models.BooleanField(default=False)),
            ],
        ),
    ]
