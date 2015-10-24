# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ReportDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('listptr', models.DecimalField(max_digits=8, decimal_places=0)),
                ('latitude', models.DecimalField(max_digits=20, decimal_places=7)),
                ('longitude', models.DecimalField(max_digits=20, decimal_places=7)),
                ('year', models.DecimalField(max_digits=5, decimal_places=0)),
                ('monday', models.DecimalField(max_digits=5, decimal_places=0)),
                ('time', models.CharField(default=b'', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ReportList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reportname', models.CharField(max_length=20)),
            ],
        ),
    ]
