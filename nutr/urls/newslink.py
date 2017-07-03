from django.conf.urls import url

from ..views import NewsLinkCreate, NewsLinkUpdate, NewsLinkDelete

urlpatterns = [
    url(r'^create/$',
        NewsLinkCreate.as_view(),
        name='nutr_newslink_create'),
url(r'^update/(?P<pk>\d+)/$',
        NewsLinkUpdate.as_view(),
        name='nutr_newslink_update'),
url(r'^delete/(?P<pk>\d+)/$',
        NewsLinkDelete.as_view(),
        name='nutr_newslink_delete'),
]

