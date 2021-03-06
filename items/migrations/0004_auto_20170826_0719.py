# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-26 07:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0003_auto_20170825_1118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadpicture',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image/'),
        ),
        migrations.AlterField(
            model_name='uploadpicture',
            name='slider_image',
            field=models.ImageField(blank=True, editable=False, null=True, upload_to='slider_image/'),
        ),
        migrations.AlterField(
            model_name='uploadpicture',
            name='thumb_image',
            field=models.ImageField(blank=True, editable=False, null=True, upload_to='thumb_image/'),
        ),
    ]
