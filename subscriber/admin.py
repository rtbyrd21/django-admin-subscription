from django.contrib import admin
from subscriber.models import Subscriber
from subscriber.models import Issue
from subscriber.models import Order
from subscriber.models import Source
from subscriber.models import Role

admin.site.register(Subscriber)
admin.site.register(Issue)
admin.site.register(Order)
admin.site.register(Source)
admin.site.register(Role)

# Register your models here.