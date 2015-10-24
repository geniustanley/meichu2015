# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0002_auto_20151024_1014'),
    ]

    operations = [
        migrations.AddField(
            model_name='reportdetail',
            name='mon_day',
            field=models.CharField(default=b'', max_length=20),
        ),
        migrations.AddField(
            model_name='reportdetail',
            name='year',
            field=models.CharField(default=b'', max_length=5),
        ),
        migrations.AlterField(
            model_name='reportdetail',
            name='time',
            field=models.CharField(default=b'', max_length=20),
        ),
    ]
