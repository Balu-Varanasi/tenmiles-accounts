# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20150329_0911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectstatistics',
            name='project',
            field=models.OneToOneField(to='accounts.Project'),
            preserve_default=True,
        ),
    ]
