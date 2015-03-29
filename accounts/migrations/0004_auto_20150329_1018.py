# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from decimal import Decimal


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20150329_0914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectstatistics',
            name='total_cost',
            field=models.DecimalField(default=Decimal('0'), verbose_name='Time Spent', max_digits=50, decimal_places=10),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='projectstatistics',
            name='total_time_spent',
            field=models.DecimalField(default=Decimal('0'), verbose_name='Time Spent', max_digits=50, decimal_places=10),
            preserve_default=True,
        ),
    ]
