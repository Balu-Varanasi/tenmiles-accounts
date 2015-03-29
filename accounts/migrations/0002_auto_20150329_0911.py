# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from decimal import Decimal


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailySprintTimeSpan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('started_at', models.DateTimeField(null=True, verbose_name='Started At')),
                ('ended_at', models.DateTimeField(null=True, verbose_name='Ended At')),
                ('hours_spent', models.DecimalField(default=Decimal('0'), verbose_name='Time Spent', max_digits=5, decimal_places=2)),
                ('project', models.ForeignKey(to='accounts.Project')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProjectStatistics',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('total_time_spent', models.DecimalField(default=Decimal('0'), verbose_name='Time Spent', max_digits=5, decimal_places=2)),
                ('total_cost', models.DecimalField(default=Decimal('0'), verbose_name='Time Spent', max_digits=5, decimal_places=2)),
                ('project', models.ForeignKey(to='accounts.Project')),
            ],
            options={
                'verbose_name': 'Project Statistics',
                'verbose_name_plural': 'Projects Statistics',
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='project',
            name='time_spent',
        ),
        migrations.AddField(
            model_name='project',
            name='end_date',
            field=models.DateField(null=True, verbose_name='End Date'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.DateField(null=True, verbose_name='Start Date'),
            preserve_default=True,
        ),
    ]
