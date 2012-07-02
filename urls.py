#!/usr/bin/env python
# encoding: utf-8

from django.conf.urls.defaults import *
from django.views.static import serve

import settings

urlpatterns = patterns('',
    (r'^resources/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    (r'^', include('core.urls')),
)
