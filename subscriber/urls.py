from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^all/$', 'subscriber.views.subscribers'),
    url(r'^get/(?P<subscriber_id>\d+)/$', 'subscriber.views.subscriber'),
    url(r'^orders/$', 'subscriber.views.orders'),

)