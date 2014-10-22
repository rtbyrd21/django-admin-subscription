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

class Issue(models.Model):
    Volume = models.DecimalField(max_digits=3, decimal_places=1)

    def __unicode__(self):
        return unicode(self.Volume)



class Subscriber(models.Model):
    name = models.CharField(max_length=200)
    address_line_one = models.CharField(max_length=200)
    address_line_two = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200)
    state_province = models.CharField(max_length=2, null=True, blank=True)
    zip = models.CharField(max_length=25)
    #is_international = models.BooleanField(default=False, help_text="hello")
    region = models.CharField(max_length=1, choices=REGION_CHOICES)
    source = models.CharField(max_length=1, choices=SOURCE_CHOICES)
    role = models.CharField(max_length=1, choices=ROLE_CHOICES)
    def __unicode__(self):
        return self.name

class Annual(models.Model):
    id = models.AutoField(primary_key=True)
    issue_1 = models.ForeignKey(Issue, related_name='first')
    issue_2 = models.ForeignKey(Issue, related_name='second')
    issue_3 = models.ForeignKey(Issue, related_name='third')
    def __unicode__(self):
        return unicode(self.id)


class Article(models.Model):
    title = models.CharField(max_length=200)
    # authors = models.ManyToManyField(User)
    abstract = models.TextField(max_length=1000, blank=True)
    full_text = models.TextField(blank=True)
    proquest_link = models.CharField(max_length=200, blank=True, null=True)
    ebsco_link = models.CharField(max_length=200, blank=True, null=True)

    def __unicode__(self):
        return self.title



class Order(models.Model):
    id = models.AutoField(primary_key=True)
    subscriber = models.ForeignKey(Subscriber)
    yearly = models.ForeignKey(Annual, default='not selected', blank=True, null=True)
    single = models.ForeignKey(Issue, default='not selected', blank=True, null=True)
    article = models.ForeignKey(Article, default='not selected', blank=True, null=True)

    def __unicode__(self):
        return unicode(self.id)

#class Invoice(models.Model)_


