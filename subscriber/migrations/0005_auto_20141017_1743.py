# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subscriber', '0004_auto_20141017_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriber',
            name='is_international',
            field=models.BooleanField(default=False, help_text=b'hello'),
        ),
    ]
