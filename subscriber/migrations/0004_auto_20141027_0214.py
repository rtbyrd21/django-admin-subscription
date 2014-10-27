# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subscriber', '0003_auto_20141026_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='annuals',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='articles',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='issues',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
