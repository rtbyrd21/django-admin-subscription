# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address_line_one', models.CharField(max_length=200)),
                ('address_line_two', models.CharField(max_length=200, null=True, blank=True)),
                ('city', models.CharField(max_length=200)),
                ('state_province', models.CharField(max_length=2, null=True, blank=True)),
                ('zip', models.CharField(max_length=25)),
                ('region', models.CharField(max_length=1, choices=[(b'D', b'Domestic'), (b'I', b'International')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Annual',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year_id', models.IntegerField(max_length=4)),
                ('start_date', models.CharField(max_length=10)),
                ('end_date', models.CharField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Annual_Issue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('annual_id', models.ForeignKey(related_name=b'annual_ids', to='subscriber.Annual')),
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
            name='Catalog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('products', models.CharField(max_length=200)),
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
                ('catalog', models.ForeignKey(related_name=b'issue_products', to='subscriber.Catalog')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('annuals', models.ForeignKey(related_name=b'annuals_ordered', blank=True, to='subscriber.Annual', null=True)),
                ('articles', models.ForeignKey(related_name=b'items_ordered', blank=True, to='subscriber.Article', null=True)),
                ('issues', models.ForeignKey(related_name=b'issues_ordered', blank=True, to='subscriber.Issue', null=True)),
                ('user', models.ForeignKey(related_name=b'who_ordered', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Order_List',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255)),
                ('user', models.ForeignKey(related_name=b'orders', to=settings.AUTH_USER_MODEL)),
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
                ('source', models.CharField(max_length=1, choices=[(b'E', b'Ebsco'), (b'S', b'Swets'), (b'D', b'Direct')])),
                ('role', models.CharField(max_length=1, choices=[(b'E', b'Editor'), (b'C', b'Contributor'), (b'B', b'Board'), (b'S', b'Staff'), (b'I', b'Individual'), (b'N', b'Institution')])),
                ('address', models.ForeignKey(related_name=b'addresses', to='subscriber.Address')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='subscriber',
            unique_together=set([('name', 'address')]),
        ),
        migrations.AlterUniqueTogether(
            name='order_list',
            unique_together=set([('user', 'name')]),
        ),
        migrations.AddField(
            model_name='article',
            name='catalog',
            field=models.ForeignKey(related_name=b'article_products', blank=True, to='subscriber.Catalog', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='annual_issue',
            name='issue_id',
            field=models.ForeignKey(related_name=b'issues', to='subscriber.Issue'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='annual',
            name='catalog',
            field=models.ForeignKey(related_name=b'annual_products', to='subscriber.Catalog'),
            preserve_default=True,
        ),
    ]
