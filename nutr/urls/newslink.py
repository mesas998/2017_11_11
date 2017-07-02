from django.conf.urls import url

from .views import NewsLinkCreate

urlpatterns = [
    url(r'^newslink/create/$',
        NewsLinkCreate.as_view(),
        name='organizer_newslink_create'),
url(r'^newslink/update/(?P<pk>\d+)/$',
        NewsLinkUpdate.as_view(),
        name='organizer_newslink_update'),
url(r'^newslink/delete/(?P<pk>\d+)/$',
        NewsLinkDelete.as_view(),
        name='organizer_newslink_delete'),
]
