# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-30 05:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0009_auto_20171030_0929'),
    ]

    operations = [
        migrations.RenameField(
            model_name='requestingdetails',
            old_name='req_date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='requestingdetails',
            old_name='req_status',
            new_name='status',
        ),
        migrations.RenameField(
            model_name='requestingdetails',
            old_name='user',
            new_name='users',
        ),
    ]