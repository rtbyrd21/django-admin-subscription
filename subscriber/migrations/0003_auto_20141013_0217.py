# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subscriber', '0002_auto_20141013_0216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='Volume',
            field=models.DecimalField(max_digits=3, decimal_places=1),
        ),
    ]
