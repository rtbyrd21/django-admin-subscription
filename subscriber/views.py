from __future__ import absolute_import

from django.views import generic
from django.db.models import Count
from braces import views

from . import models
from . import forms
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from subscriber.models import Subscriber
from subscriber.models import Order
from subscriber.models import Catalog
from subscriber.models import Order_List

# Create your views here.

class RestrictToUserMixin(object):
    def get_queryset(self):
        queryset = super(RestrictToUserMixin, self).get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset

class OrderListListView(
    views.LoginRequiredMixin,
    RestrictToUserMixin,
    generic.ListView
):
    model = Order
    template_name = 'orderlist.html'

    def get_queryset(self):
        queryset = super(OrderListListView, self).get_queryset()
        queryset = queryset.annotate(order_count=Count('select'))
        return queryset


class OrderListDetailView(
    views.LoginRequiredMixin,
    # views.PrefetchRelatedMixin,
    RestrictToUserMixin,
    generic.DetailView
):
    model = Order_List
    template_name = 'order_list_detail.html'
    # prefetch_related = ('orders',)


class OrderListCreateView(
    views.LoginRequiredMixin,
    views.SetHeadlineMixin,
    generic.CreateView
):
    form_class = forms.OrderListForm
    headline = 'Create'
    model = Order
    template_name = 'ordercreate.html'


    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super(OrderListCreateView, self).form_valid(form)


class TalkListScheduleView(
    views.PrefetchRelatedMixin,
    generic.ListView
):
    model = Order
    prefetch_related = ('user',)
    template_name = 'mailing.html'







def subscribers(request):
    return render_to_response('subscribers.html',
                             {'subscribers': Subscriber.objects.all()})

def subscriber(request, subscriber_id=1):
    return render_to_response('subscriber.html',
                             {'subscriber': Subscriber.objects.get(id=subscriber_id)})

def orders(request):
    return render_to_response('order.html',
                             {'orders': Order.objects.all()})

def products(request):
    return render_to_response('products.html',
                             {'catalogs': Catalog.objects.all()})

def reverse(request):
    return  render_to_response('reverse.html',
                             {'bart': User.objects.filter(order__select='2')})