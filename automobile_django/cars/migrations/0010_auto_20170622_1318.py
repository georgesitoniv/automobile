# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-22 13:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0009_auto_20170622_1215'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='car',
            options={'ordering': ('order',)},
        ),
        migrations.AddField(
            model_name='car',
            name='order',
            field=models.PositiveIntegerField(db_index=True, default=0, editable=False),
            preserve_default=False,
        ),
    ]