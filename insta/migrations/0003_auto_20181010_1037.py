# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-10 07:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0002_auto_20181009_2022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.CharField(max_length=30),
        ),
    ]
