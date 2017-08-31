# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-31 09:41
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('items', '0011_uploadpicture_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadpicture',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
