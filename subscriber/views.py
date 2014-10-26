from django.shortcuts import render_to_response
from subscriber.models import Subscriber
from subscriber.models import Order
from subscriber.models import Catalog

# Create your views here.

def subscribers(request):
    return render_to_response('subscribers.html',
                             {'subscribers': Subscriber.objects.all()})

def subscriber(request, subscriber_id=1):
    return render_to_response('subscriber.html',
                             {'subscriber': Subscriber.objects.get(id=subscriber_id)})

def orders(request):
    return render_to_response('order.html',
                             {'order': Order.objects.all()})

def products(request):
    return render_to_response('products.html',
                             {'catalogs': Catalog.objects.all()})