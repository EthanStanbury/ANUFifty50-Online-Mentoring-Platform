# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-24 04:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to='blog_images'),
        ),
    ]
