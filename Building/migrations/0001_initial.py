# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-21 12:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='building',
            fields=[
                ('building_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('perhour', models.BigIntegerField()),
                ('cost', models.BigIntegerField()),
                ('multipleir', models.FloatField()),
                ('requiredxp', models.BigIntegerField()),
            ],
        ),
    ]