# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-22 03:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0020_auto_20170722_1342'),
    ]

    operations = [
        migrations.RenameField(
            model_name='document',
            old_name='Name',
            new_name='Filename',
        ),
        migrations.RenameField(
            model_name='document',
            old_name='Mentee_Mentor',
            new_name='Role',
        ),
    ]
