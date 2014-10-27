from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify
#from time import time


# Create your models here.

REGION_CHOICES = (
    ('D', 'Domestic'),
    ('I', 'International')
)

SOURCE_CHOICES = (
    ('E', 'Ebsco'),
    ('S', 'Swets'),
    ('D', 'Direct')
)

ROLE_CHOICES = (
    ('E', 'Editor'),
    ('C', 'Contributor'),
    ('B', 'Board'),
    ('S', 'Staff'),
    ('I', 'Individual'),
    ('N', 'Institution'),
)


class Order_List(models.Model):
    user = models.ForeignKey(User, related_name='orders')
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)

    class Meta:
        unique_together = ('user', 'name')

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Order_List, self).save(*args, **kwargs)


class Role(models.Model):
    role = models.CharField(max_length=100)

    def __unicode__(self):
        return self.role

class Catalog(models.Model):
    products = models.CharField(max_length=200)

    def __unicode__(self):
        return self.products

class Issue(models.Model):
    catalog = models.ForeignKey(Catalog, related_name='issue_products')
    Volume = models.DecimalField(max_digits=3, decimal_places=1)

    def __unicode__(self):
        return unicode(self.Volume)

class Address(models.Model):
    address_line_one = models.CharField(max_length=200)
    address_line_two = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200)
    state_province = models.CharField(max_length=2, null=True, blank=True)
    zip = models.CharField(max_length=25)
    region = models.CharField(max_length=1, choices=REGION_CHOICES)
    def __unicode__(self):
        return self.address_line_one


class Subscriber(models.Model):
    name = models.CharField(max_length=200)
    address = models.ForeignKey(Address, related_name='addresses')
    source = models.CharField(max_length=1, choices=SOURCE_CHOICES)
    role = models.CharField(max_length=1, choices=ROLE_CHOICES)

    class Meta:
        unique_together = ('name', 'address')

    def __unicode__(self):
        return self.name



class Annual(models.Model):
    catalog = models.ForeignKey(Catalog, related_name='annual_products')
    year_id = models.IntegerField(max_length=4)
    start_date = models.CharField(max_length=10)
    end_date = models.CharField(max_length=10)
    def __unicode__(self):
        return unicode(self.year_id)



class Annual_Issue(models.Model):
    annual_id = models.ForeignKey(Annual, related_name='annual_ids')
    issue_id = models.ForeignKey(Issue, related_name='issues')
    def __unicode__(self):
        return self.annual_id



class Article(models.Model):
    catalog = models.ForeignKey(Catalog, related_name='article_products', blank=True, null=True)
    title = models.CharField(max_length=200)
    abstract = models.TextField(max_length=1000, blank=True)
    full_text = models.TextField(blank=True)
    proquest_link = models.CharField(max_length=200, blank=True, null=True)
    ebsco_link = models.CharField(max_length=200, blank=True, null=True)

    def __unicode__(self):
        return self.title



class Order(models.Model):
    user = models.ForeignKey(User, related_name='who_ordered')
   # annuals = models.CharField(max_length=200, blank=True, null=True)
   # issues = models.CharField(max_length=200, blank=True, null=True)
   # articles = models.CharField(max_length=200, blank=True, null=True)

    annuals = models.ForeignKey(Annual, related_name='annuals_ordered', blank=True, null=True)
    issues = models.ForeignKey(Issue, related_name='issues_ordered', blank=True, null=True)
    articles = models.ForeignKey(Article, related_name='items_ordered', blank=True, null=True)


  #  annuals = models.ForeignKey(Catalog, related_name='annuals_ordered', blank=True, null=True)
  #  issues = models.ForeignKey(Catalog, related_name='issues_ordered', blank=True, null=True)
  #  articles = models.ForeignKey(Catalog, related_name='items_ordered', blank=True, null=True)






#class Invoice(models.Model)_


