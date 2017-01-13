# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-13 16:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_parser', '0005_auto_20170113_1443'),
    ]

    operations = [
        migrations.CreateModel(
            name='ParserCsv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload', models.FileField(blank=True, upload_to='')),
            ],
        ),
        migrations.RenameModel(
            old_name='Movie',
            new_name='Csv',
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]