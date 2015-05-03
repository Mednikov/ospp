# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ospp_app', '0005_project_archive'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='create_date',
        ),
        migrations.AddField(
            model_name='project',
            name='date_create',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='date_modified',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
