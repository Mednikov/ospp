# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ospp_app', '0002_auto_20150503_0139'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('text', models.TextField()),
                ('project', models.ForeignKey(to='ospp_app.Project')),
            ],
            options={
                'db_table': 'comment',
            },
        ),
    ]
