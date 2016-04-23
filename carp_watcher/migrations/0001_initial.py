# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data_Stream',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('velocity', models.DecimalField(max_digits=7, decimal_places=4)),
                ('discharge', models.DecimalField(max_digits=7, decimal_places=2)),
                ('day', models.DateTimeField()),
            ],
            options={
                'ordering': ('stream', 'day'),
            },
        ),
        migrations.CreateModel(
            name='Data_Stream_Temp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('temp', models.IntegerField()),
                ('day', models.DateTimeField()),
            ],
            options={
                'ordering': ('stream', 'day'),
            },
        ),
        migrations.CreateModel(
            name='Fish',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('coefficient', models.DecimalField(max_digits=10, decimal_places=2)),
                ('exponent', models.DecimalField(max_digits=10, decimal_places=8)),
            ],
        ),
        migrations.CreateModel(
            name='Stream',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('coeff_x2', models.DecimalField(default=0, max_digits=7, decimal_places=4)),
                ('coeff_x', models.DecimalField(default=0, max_digits=7, decimal_places=4)),
                ('coeff_con', models.DecimalField(default=0, max_digits=7, decimal_places=4)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.AddField(
            model_name='data_stream_temp',
            name='stream',
            field=models.ForeignKey(to='carp_watcher.Stream'),
        ),
        migrations.AddField(
            model_name='data_stream',
            name='stream',
            field=models.ForeignKey(to='carp_watcher.Stream'),
        ),
        migrations.AlterUniqueTogether(
            name='data_stream_temp',
            unique_together=set([('stream', 'day')]),
        ),
        migrations.AlterUniqueTogether(
            name='data_stream',
            unique_together=set([('stream', 'day')]),
        ),
    ]
