# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carp_watcher', '0007_auto_20160424_0307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data_stream',
            name='temp',
            field=models.DecimalField(max_digits=7, decimal_places=4),
        ),
    ]
