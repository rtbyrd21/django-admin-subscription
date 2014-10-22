# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Annual',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('abstract', models.TextField(max_length=1000, blank=True)),
                ('full_text', models.TextField(blank=True)),
                ('proquest_link', models.CharField(max_length=200, null=True, blank=True)),
                ('ebsco_link', models.CharField(max_length=200, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Volume', models.DecimalField(max_digits=3, decimal_places=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('article', models.ForeignKey(default=b'not selected', blank=True, to='subscriber.Article', null=True)),
                ('single', models.ForeignKey(default=b'not selected', blank=True, to='subscriber.Issue', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('role', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('address_line_one', models.CharField(max_length=200)),
                ('address_line_two', models.CharField(max_length=200, null=True, blank=True)),
                ('city', models.CharField(max_length=200)),
                ('state_province', models.CharField(max_length=2, null=True, blank=True)),
                ('zip', models.CharField(max_length=25)),
                ('region', models.CharField(max_length=1, choices=[(b'D', b'Domestic'), (b'I', b'International')])),
                ('source', models.CharField(max_length=1, choices=[(b'E', b'Ebsco'), (b'S', b'Swets'), (b'D', b'Direct')])),
                ('role', models.CharField(max_length=1, choices=[(b'E', b'Editor'), (b'C', b'Contributor'), (b'B', b'Board'), (b'S', b'Staff'), (b'I', b'Individual'), (b'N', b'Institution')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='order',
            name='subscriber',
            field=models.ForeignKey(to='subscriber.Subscriber'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order',
            name='yearly',
            field=models.ForeignKey(default=b'not selected', blank=True, to='subscriber.Annual', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='annual',
            name='issue_1',
            field=models.ForeignKey(related_name=b'first', to='subscriber.Issue'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='annual',
            name='issue_2',
            field=models.ForeignKey(related_name=b'second', to='subscriber.Issue'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='annual',
            name='issue_3',
            field=models.ForeignKey(related_name=b'third', to='subscriber.Issue'),
            preserve_default=True,
        ),
    ]
