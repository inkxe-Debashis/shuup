# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-12-12 03:22
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0006_auto_20160623_1627'),
        ('shuup', '0021_country_limit_behavior_component'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='favicon',
            field=filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='shop_favicons', to='filer.Image'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='logo',
            field=filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='shop_logos', to='filer.Image'),
        ),
    ]