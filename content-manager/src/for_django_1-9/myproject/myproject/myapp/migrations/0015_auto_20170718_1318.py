# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-18 03:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_auto_20170718_1311'),
    ]

    operations = [
        migrations.RenameField(
            model_name='week',
            old_name='week',
            new_name='test',
        ),
    ]