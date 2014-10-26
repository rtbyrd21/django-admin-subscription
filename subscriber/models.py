from django.db import models
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
    def __unicode__(self):
        return self.name



class Annual(models.Model):
    catalog = models.ForeignKey(Catalog, related_name='annual_products')
    year_id = models.IntegerField(max_length=4)
    start_date = models.CharField(max_length=6)
    end_date = models.CharField(max_length=6)
    def __unicode__(self):
        return unicode(self.year_id)

    #def __unicode__(self):
    #    return unicode(self.id)

class Annual_Issue(models.Model):
    annual_id = models.ForeignKey(Annual, related_name='annual_ids')
    issue_id = models.ForeignKey(Issue, related_name='issues')
    def __unicode__(self):
        return self.annual_id



class Article(models.Model):
    catalog = models.ForeignKey(Catalog, related_name='article_products')
    title = models.CharField(max_length=200)
    abstract = models.TextField(max_length=1000, blank=True)
    full_text = models.TextField(blank=True)
    proquest_link = models.CharField(max_length=200, blank=True, null=True)
    ebsco_link = models.CharField(max_length=200, blank=True, null=True)

    def __unicode__(self):
        return self.title


class Order_Lines(models.Model):
    order_line_1 = models.CharField(max_length=200)
    order_line_2 = models.CharField(max_length=200)
    order_line_3 = models.CharField(max_length=200)
    order_line_4 = models.CharField(max_length=200)
    order_line_5 = models.CharField(max_length=200)

    def __unicode__(self):
        return self.order_line_1


class Order(models.Model):
    subscriber = models.ForeignKey(Subscriber)
    order_lines = models.ForeignKey(Order_Lines)

    def __unicode__(self):
        return self.subscriber





#class Invoice(models.Model)_


