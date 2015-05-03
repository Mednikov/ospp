# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('ospp_app', '0006_auto_20150503_0250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='date_create',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='project',
            name='date_modified',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
