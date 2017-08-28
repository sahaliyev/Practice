# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-25 11:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_auto_20170825_0717'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadpicture',
            name='slider_image',
            field=models.ImageField(blank=True, null=True, upload_to='slider/'),
        ),
        migrations.AddField(
            model_name='uploadpicture',
            name='thumb_image',
            field=models.ImageField(blank=True, null=True, upload_to='small/'),
        ),
        migrations.AlterField(
            model_name='uploadpicture',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='orginal/'),
        ),
    ]