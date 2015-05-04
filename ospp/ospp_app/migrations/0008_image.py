# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ospp_app', '0007_auto_20150503_0306'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('image', models.ImageField(upload_to='')),
                ('project', models.ForeignKey(to='ospp_app.Project')),
            ],
            options={
                'db_table': 'image',
            },
        ),
    ]
