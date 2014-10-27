# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subscriber', '0005_auto_20141027_0231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='annuals',
            field=models.ForeignKey(related_name=b'annuals_ordered', blank=True, to='subscriber.Annual', null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='articles',
            field=models.ForeignKey(related_name=b'items_ordered', blank=True, to='subscriber.Article', null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='issues',
            field=models.ForeignKey(related_name=b'issues_ordered', blank=True, to='subscriber.Issue', null=True),
        ),
    ]
