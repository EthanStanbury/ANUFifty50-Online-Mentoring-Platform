# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-20 22:45
from __future__ import unicode_literals

from django.db import migrations, models
import myproject.myapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0018_auto_20170718_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='Mentee_Mentor',
            field=models.CharField(choices=[('Mentee', 'Mentee'), ('Mentee', 'Mentor'), ('Training', 'Training')], default='Mentee', max_length=25),
        ),
        migrations.AlterField(
            model_name='document',
            name='Week',
            field=models.CharField(choices=[('Week1', 'Week_1'), ('Week2', 'Week_2'), ('Week2', 'Week_3'), ('Week2', 'Week_4')], default='Week1', max_length=10),
        ),
        migrations.AlterField(
            model_name='document',
            name='docfile',
            field=models.FileField(upload_to=myproject.myapp.models.Document.choices_location),
        ),
    ]