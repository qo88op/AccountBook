# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-21 06:53
from __future__ import unicode_literals

from django.db import migrations, models
import django_hstore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accountbook', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='bill_type',
            field=models.IntegerField(choices=[(1, '\u6536\u5165'), (2, '\u652f\u51fa')], default=2, verbose_name='\u7c7b\u578b'),
        ),
        migrations.AddField(
            model_name='bill',
            name='data',
            field=django_hstore.fields.DictionaryField(blank=True, verbose_name='\u6570\u636e'),
        ),
        migrations.AddField(
            model_name='category',
            name='data',
            field=django_hstore.fields.SerializedDictionaryField(blank=True, verbose_name='\u6570\u636e'),
        ),
    ]
