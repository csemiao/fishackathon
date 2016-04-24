# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carp_watcher', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stream',
            name='lat',
            field=models.DecimalField(default=0, max_digits=12, decimal_places=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stream',
            name='long',
            field=models.DecimalField(default=0, max_digits=12, decimal_places=9),
            preserve_default=False,
        ),
    ]
