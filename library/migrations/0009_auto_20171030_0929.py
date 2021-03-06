# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-30 03:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0008_auto_20171030_0906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lendingdetails',
            name='req_status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], max_length=30),
        ),
        migrations.AlterField(
            model_name='requestingdetails',
            name='req_status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], max_length=30),
        ),
    ]
