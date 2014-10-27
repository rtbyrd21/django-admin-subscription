# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subscriber', '0004_auto_20141027_0214'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Order_Lines',
        ),
        migrations.AlterField(
            model_name='annual',
            name='end_date',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='annual',
            name='start_date',
            field=models.CharField(max_length=10),
        ),
    ]
