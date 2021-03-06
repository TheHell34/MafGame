# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-17 09:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Player', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='building',
            fields=[
                ('building_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('perminute', models.BigIntegerField()),
                ('cost', models.BigIntegerField()),
                ('multiplier', models.FloatField()),
                ('requiredxp', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='player_building',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('level', models.IntegerField()),
                ('perminute', models.BigIntegerField()),
                ('cost', models.BigIntegerField()),
                ('building_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Building.building')),
                ('player_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Player.player')),
            ],
        ),
    ]
