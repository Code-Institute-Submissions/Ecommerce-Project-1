# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-01-27 12:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20200127_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(max_length=254),
        ),
    ]