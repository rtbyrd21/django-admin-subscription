from django.contrib import admin
from subscriber.models import Subscriber
from subscriber.models import Issue
from subscriber.models import Annual
from subscriber.models import Order
from subscriber.models import Article
from subscriber.models import Address
from subscriber.models import Catalog
from subscriber.models import Annual_Issue
from subscriber.models import Order_List


class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('name', 'source', 'role')
    search_fields = ['name']

class AnnualAdmin(admin.ModelAdmin):
    list_display = ('id',)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id',)

    def get_name(self, obj):
        return obj.subscriber.name
    get_name.short_description = 'Name'
    get_name.admin_order_field = 'subscriber__name'

    def get_yearly(self, obj):
        return obj.yearly.id
    get_yearly.short_description = 'Annual Id'
    get_yearly.admin_order_field = 'annual__id'

    def get_single(self, obj):
        return obj.single.Volume
    get_single.short_description = 'Individual Issues'
    get_single.admin_order_field = 'single__id'

    def get_article(self, obj):
        return obj.article.title
    get_article.short_description = 'Article Title'
    get_single.admin_order_field = 'article__title'



admin.site.register(Subscriber, SubscriberAdmin)
admin.site.register(Issue)
admin.site.register(Address)
admin.site.register(Catalog)
admin.site.register(Annual, AnnualAdmin)
admin.site.register(Annual_Issue)
admin.site.register(Article)
admin.site.register(Order, OrderAdmin)
admin.site.register(Order_List)

# Register your models here.