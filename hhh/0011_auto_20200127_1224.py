# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-01-27 12:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20200127_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(max_length=254, null=True),
        ),
    ]
