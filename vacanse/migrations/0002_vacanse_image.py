# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-17 06:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacanse', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacanse',
            name='image',
            field=models.ImageField(default='vacanse/noimagefound.jpg', upload_to='vacance'),
        ),
    ]
