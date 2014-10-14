from django.db import models
# Create your models here.

class Source(models.Model):
    source = models.CharField(max_length=100)

    def __unicode__(self):
        return self.source

class Role(models.Model):
    role = models.CharField(max_length=100)

    def __unicode__(self):
        return self.role

class Subscriber(models.Model):
    name = models.CharField(max_length=200)
    address_line_one = models.CharField(max_length=200)
    address_line_two = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200)
    state_province = models.CharField(max_length=2, null=True, blank=True)
    zip = models.CharField(max_length=25)
    international = models.BooleanField(default=False)
    source = models.ForeignKey(Source)
    role = models.ForeignKey(Role)

    def __unicode__(self):
        return self.name

class Issue(models.Model):
    Volume = models.DecimalField(max_digits=3, decimal_places=1)

    def __unicode__(self):
        return unicode(self.Volume)

class Order(models.Model):
    subscriber = models.ForeignKey(Subscriber)
    issue = models.ForeignKey(Issue)

    def __unicode__(self):
        return unicode(self.subscriber)




