# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-17 12:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ask', '0006_auto_20160517_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_avatar',
            field=models.ImageField(upload_to=b''),
        ),
    ]