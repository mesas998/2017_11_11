""" URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.sitemaps.views import (
    index as site_index_view,
    sitemap as sitemap_view)
from user import urls as user_urls
from nutr.views import homepage, upload
from nutr.models import POC
from .views import redirect_root
from nutr.urls import poc as poc_urls, tag as tag_urls
from blog import urls as blog_urls
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponseRedirect, HttpResponse
from .sitemaps import sitemaps as sitemaps_dict

admin.site.site_header = 'POC Admin'
admin.site.site_title = 'POC Organizer Site Admin'

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include(blog_urls)),
    url(r'^sitemap\.xml$',
        site_index_view,
        {'sitemaps': sitemaps_dict},
        name='sitemap'),
    url(r'^sitemap-(?P<section>.+)\.xml$',
        sitemap_view,
        {'sitemaps': sitemaps_dict},
        name='sitemap-sections'),
    #rl(r'^$', redirect_root),
    url(r'^$', homepage),
    url(r'^poc/', include(poc_urls)),
    url(r'^tag/', include(tag_urls)),
    url(r'^upload/',upload),
    url(r'^user/',
        include(
            user_urls,
            app_name='user',
            namespace='dj-auth')),
    url(r'^googled12693e979b29607\.html$', lambda r: HttpResponse("google-site-verification: googled12693e979b29607.html")),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
] # static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

