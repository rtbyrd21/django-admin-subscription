# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subscriber', '0006_subscriber_region'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscriber',
            name='is_international',
        ),
    ]
