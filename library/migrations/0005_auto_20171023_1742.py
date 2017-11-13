# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-23 12:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_author_author_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='books',
            name='review',
        ),
        migrations.RemoveField(
            model_name='photos',
            name='book_id',
        ),
        migrations.RemoveField(
            model_name='reviews',
            name='book_id',
        ),
        migrations.AddField(
            model_name='photos',
            name='book',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='library.Books'),
        ),
        migrations.AddField(
            model_name='reviews',
            name='book',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='library.Books'),
        ),
        migrations.AlterField(
            model_name='photos',
            name='photos',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='review',
            field=models.TextField(max_length=500, null=True),
        ),
    ]
