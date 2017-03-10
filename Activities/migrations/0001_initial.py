# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-10 22:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='activity',
            fields=[
                ('activity_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('cost', models.BigIntegerField()),
                ('reward', models.BigIntegerField()),
            ],
        ),
    ]
