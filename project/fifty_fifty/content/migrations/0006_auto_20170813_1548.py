# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-13 05:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0005_auto_20170803_0541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentee',
            name='docfile',
            field=models.FileField(null=True, upload_to='FileUploads/mentee/'),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='docfile',
            field=models.FileField(null=True, upload_to='FileUploads/mentor/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='docfile',
            field=models.FileField(null=True, upload_to='FileUploads/news/'),
        ),
        migrations.AlterField(
            model_name='training',
            name='docfile',
            field=models.FileField(null=True, upload_to='FileUploads/training/'),
        ),
    ]
