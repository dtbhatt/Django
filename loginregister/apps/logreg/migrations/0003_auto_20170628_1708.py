# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-28 17:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logreg', '0002_user_birthdate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='lastName',
            new_name='alias',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='firstName',
            new_name='name',
        ),
    ]
