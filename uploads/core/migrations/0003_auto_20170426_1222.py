# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-26 12:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20160801_0816'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='description',
        ),
        migrations.RemoveField(
            model_name='document',
            name='uploaded_at',
        ),
    ]
