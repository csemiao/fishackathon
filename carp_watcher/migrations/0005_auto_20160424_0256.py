# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carp_watcher', '0004_auto_20160424_0148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fish',
            name='coefficient',
            field=models.DecimalField(max_digits=10, decimal_places=7),
        ),
        migrations.AlterField(
            model_name='fish',
            name='exponent',
            field=models.DecimalField(max_digits=10, decimal_places=5),
        ),
    ]
