# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-24 06:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_question_question_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_body',
            field=models.TextField(default='', max_length=300),
        ),
    ]