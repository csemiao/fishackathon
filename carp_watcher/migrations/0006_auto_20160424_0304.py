# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carp_watcher', '0005_auto_20160424_0256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fish',
            name='exponent',
            field=models.DecimalField(max_digits=10, decimal_places=4),
        ),
    ]
