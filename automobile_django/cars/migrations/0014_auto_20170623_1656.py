# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-23 16:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0013_remove_car_slot_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='color',
            name='name',
            field=models.CharField(max_length=250, unique=True),
        ),
    ]
