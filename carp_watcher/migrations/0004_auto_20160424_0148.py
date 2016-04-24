# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carp_watcher', '0003_auto_20160424_0040'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='data_stream_temp',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='data_stream_temp',
            name='stream',
        ),
        migrations.RemoveField(
            model_name='data_stream',
            name='discharge',
        ),
        migrations.RemoveField(
            model_name='stream',
            name='coeff_con',
        ),
        migrations.RemoveField(
            model_name='stream',
            name='coeff_x',
        ),
        migrations.RemoveField(
            model_name='stream',
            name='coeff_x2',
        ),
        migrations.AddField(
            model_name='data_stream',
            name='temp',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Data_Stream_Temp',
        ),
    ]
