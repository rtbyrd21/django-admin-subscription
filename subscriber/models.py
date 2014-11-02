from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.dispatch import receiver
from django.db.models.signals import post_save
from itertools import chain

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
    name = models.CharField(max_length=100)
    price = models.IntegerField()

    def __unicode__(self):
        return self.name


class Issue(models.Model):
    catalog = models.OneToOneField(Catalog, related_name='issue_products', blank=True, null=True)
    issue_number = models.DecimalField(max_digits=3, decimal_places=1)
    date = models.DateTimeField(auto_now_add=True, blank=True)

    def __unicode__(self):
        return unicode(self.issue_number)

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
    catalog = models.OneToOneField(Catalog, blank=True, null=True, related_name='annual_products')
    year_id = models.IntegerField(max_length=4)
    start_date = models.CharField(max_length=10)
    end_date = models.CharField(max_length=10)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    def __unicode__(self):
        return unicode(self.year_id)




class Annual_Issue(models.Model):
    annual_id = models.ForeignKey(Annual, related_name='annual_ids')
    issue_id = models.ForeignKey(Issue, related_name='issues')
    date = models.DateTimeField(auto_now_add=True, blank=True)
    def __unicode__(self):
        return unicode(self.annual_id)



class Article(models.Model):
    catalog = models.OneToOneField(Catalog, related_name='article_products', blank=True, null=True)
    title = models.CharField(max_length=200)
    abstract = models.TextField(max_length=1000, blank=True)
    full_text = models.TextField(blank=True)
    proquest_link = models.CharField(max_length=200, blank=True, null=True)
    ebsco_link = models.CharField(max_length=200, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True, blank=True)

    def __unicode__(self):
        return unicode(self.title)




@receiver(post_save, sender=Article)
def create_catalog_article(sender, **kwargs):
    if kwargs.get('created', False):
        Catalog.objects.get_or_create(name=kwargs.get('instance'), price='10')

@receiver(post_save, sender=Issue)
def create_catalog_issue(sender, **kwargs):
    if kwargs.get('created', False):
        Catalog.objects.get_or_create(name=kwargs.get('instance'), price='5')

@receiver(post_save, sender=Annual)
def create_catalog_annual(sender, **kwargs):
    if kwargs.get('created', False):
        Catalog.objects.get_or_create(name=kwargs.get('instance'), price='30')

@receiver(post_save, sender=Catalog)
def attach_catalog(sender, **kwargs):
    if kwargs.get('created', False):
        article_list = Article.objects.all()
        issue_list = Issue.objects.all()
        annual_list = Annual.objects.all()
        result_list = list(chain(article_list, issue_list, annual_list))
        b = max(result_list, key=lambda x: x.date)
        if Article.objects.exists():
            Article.objects.filter(pk=b.id).update(catalog=kwargs.get('instance'))
        if Issue.objects.exists():
            Issue.objects.filter(pk=b.id).update(catalog=kwargs.get('instance'))
        if Annual.objects.exists():
            Annual.objects.filter(pk=b.id).update(catalog=kwargs.get('instance'))






class Order(models.Model):
    user = models.ForeignKey(User)
    select = models.ManyToManyField(Catalog, blank=True, null=True)

    def __unicode__(self):
        return unicode(self.user)





















   # def save(self, *args, **kwargs):
    #     u = super(Article, self).save(*args, **kwargs)
    #     Catalog.objects.get_or_create(name=u.title)
    #     return u

    # def create(self):
    #     cat = Catalog.create(title = self.title)
    #     cat.save()

    # def save(self, *args, **kwargs):
    #     super(Article, self).save(*args, **kwargs)
    #     self.catalog.name = 'value'
    #     self.catalog.save()

    # method for updating
    # def create_catalog(sender, instance, created, **kwargs):
    #     if instance and created:
    #      #create article object, and associate
    #
    #
    #     post_save.connect(create_catalog, sender=Article)

    # self.full_text = self.title
    # super(Article, self).save(*args, **kwargs)

 # b = result_list.latest('date')
        # b = Article.objects.latest('date')