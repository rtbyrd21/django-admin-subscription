from django.conf.urls import patterns, include, url

from views import OrderListListView, OrderListDetailView, OrderListCreateView

urlpatterns = patterns('',

    url(r'^all/$', 'subscriber.views.subscribers'),
    url(r'^get/(?P<subscriber_id>\d+)/$', 'subscriber.views.subscriber'),
    url(r'^orders/$', 'subscriber.views.orders'),
    url(r'^products/$', 'subscriber.views.products'),
    url(r'^orders/$', 'subscriber.views.orders'),
    url(r'^orderlist/$', OrderListListView.as_view(), name='list'),
    url(r'd/(?P<slug>[-\w]+)/$', OrderListDetailView.as_view(), name="detail"),
    url(r'^create/$', OrderListCreateView.as_view(), name='create'),

)