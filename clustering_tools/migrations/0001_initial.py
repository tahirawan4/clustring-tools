# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2017-12-13 12:51
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Respons',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, null=True)),
                ('orig_text', models.TextField(blank=True, null=True)),
                ('prob', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), blank=True, size=None)),
            ],
        ),
        migrations.CreateModel(
            name='SemanticLabel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intent', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='respons',
            name='manual_semantic_label',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clustering_tools.SemanticLabel'),
        ),
    ]
