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
                ('positionX', models.DecimalField(max_digits=8, decimal_places=3)),
                ('positionY', models.DecimalField(max_digits=8, decimal_places=3)),
                ('time', models.CharField(max_length=20)),
                ('listptr', models.DecimalField(max_digits=3, decimal_places=0)),
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
