# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-24 15:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Travel_Dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='plan',
            field=models.CharField(default='', max_length=1000),
            preserve_default=False,
        ),
    ]
