# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carp_watcher', '0002_auto_20160423_2047'),
    ]

    operations = [
        migrations.AddField(
            model_name='data_stream',
            name='spike',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='stream',
            name='length',
            field=models.DecimalField(default=1, max_digits=10, decimal_places=2),
            preserve_default=False,
        ),
    ]
