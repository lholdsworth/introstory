# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-13 17:13
from __future__ import unicode_literals

from django.db import migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='standard_video',
            field=embed_video.fields.EmbedVideoField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='profile',
            name='vr_video',
            field=embed_video.fields.EmbedVideoField(blank=True, max_length=255),
        ),
    ]
