# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-30 07:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0012_requestingdetails_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='lendingdetails',
            name='final_req',
            field=models.CharField(choices=[('Approved', 'Approved'), ('Rejected', 'Rejected')], max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='requestingdetails',
            name='final_status',
            field=models.CharField(choices=[('Approved', 'Approved'), ('Rejected', 'Rejected')], max_length=30, null=True),
        ),
    ]
