# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-03 13:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20180503_0758'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collection',
            name='editorial',
        ),
        migrations.RemoveField(
            model_name='pdf',
            name='collection',
        ),
        migrations.DeleteModel(
            name='Collection',
        ),
    ]
