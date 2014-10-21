# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subscriber', '0005_auto_20141017_1743'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriber',
            name='region',
            field=models.CharField(default='ok', max_length=1, choices=[(b'D', b'Domestic'), (b'I', b'International')]),
            preserve_default=False,
        ),
    ]
