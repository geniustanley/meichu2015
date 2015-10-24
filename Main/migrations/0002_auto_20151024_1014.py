# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportdetail',
            name='latitude',
            field=models.DecimalField(max_digits=20, decimal_places=7),
        ),
        migrations.AlterField(
            model_name='reportdetail',
            name='longtitude',
            field=models.DecimalField(max_digits=20, decimal_places=7),
        ),
    ]
