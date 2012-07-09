# encoding: utf-8

from django.conf.urls.defaults import *

urlpatterns = patterns('core.views',
    url(r'^$', 'public.index', name="index"),
    url(r'^contact/$', 'public.contact', name="contact"),
)
