# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-01 06:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='plan_finish',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='plan_start',
            field=models.DateTimeField(null=True),
        ),
    ]