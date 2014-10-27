# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subscriber', '0006_auto_20141027_0329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='catalog',
            field=models.ForeignKey(related_name=b'article_products', blank=True, to='subscriber.Catalog', null=True),
        ),
    ]
