# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-20 22:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='Question_Content',
            new_name='question_Content',
        ),
        migrations.AlterField(
            model_name='post',
            name='publishing_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Yayımlanma Tarihi'),
        ),
    ]
