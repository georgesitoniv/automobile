# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-17 08:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slot',
            name='car',
        ),
        migrations.AddField(
            model_name='car',
            name='slot_number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='Slot',
        ),
    ]
