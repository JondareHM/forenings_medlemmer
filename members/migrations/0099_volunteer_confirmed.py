# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2018-01-30 17:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0098_activity_union'),
    ]

    operations = [
        migrations.AddField(
            model_name='volunteer',
            name='confirmed',
            field=models.DateTimeField(blank=True, default=None, null=True, verbose_name='Bekræftet'),
        ),
    ]