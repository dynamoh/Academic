# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-09-12 12:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acadmodule', '0021_auto_20190911_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_name',
            field=models.CharField(max_length=256, unique=True),
        ),
    ]