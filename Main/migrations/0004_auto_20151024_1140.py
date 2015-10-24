# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0003_auto_20151024_1117'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reportdetail',
            old_name='mon_day',
            new_name='monday',
        ),
    ]
