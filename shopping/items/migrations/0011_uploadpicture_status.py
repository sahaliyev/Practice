# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-30 15:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0010_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadpicture',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]