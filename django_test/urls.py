from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()


from views import HomePageView, SignUpView, LoginView, logout_view

urlpatterns = patterns('',

    (r'^subscribers/', include('subscriber.urls')),
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'accounts/register/$', SignUpView.as_view(), name='signup'),
    url(r'accounts/login/$', LoginView.as_view(), name='login'),
    url(r'accounts/logout/$', logout_view, name='logout'),
    #url(r'^hello/$', 'subscriber.views.hello'),
    #url(r'^hello_template/$', 'subscriber.views.hello_template'),
    #url(r'^hello_template_simple/$', 'subscriber.views.hello_template_simple'),
    url(r'^admin/', include(admin.site.urls)),

    #auth



    # url(r'^accounts/login/$', 'django_test.views.login'),
    # url(r'^accounts/auth/$', 'django_test.views.auth_view'),
    # url(r'^accounts/logout/$', 'django_test.views.logout'),
    # url(r'^accounts/loggedin/$', 'django_test.views.loggedin'),
    # url(r'^accounts/invalid/$', 'django_test.views.invalid_login'),
    # url(r'^accounts/register/$', 'django_test.views.register_user'),
    # url(r'^accounts/register_success/$', 'django_test.views.register_success'),



)
