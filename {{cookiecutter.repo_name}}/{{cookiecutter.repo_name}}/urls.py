# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pro.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)