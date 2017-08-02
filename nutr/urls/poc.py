from django.conf.urls import url
from ..views import POCList, poc_detail, poc_create, POCCreate, POCUpdate, POCDelete, NewsLinkCreate, NewsLinkUpdate, NewsLinkDelete, upload
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^$', POCList.as_view(), name='nutr_poc_list'),
    url(r'^create/$', POCCreate.as_view(), name='nutr_poc_create'),
    url(r'^upload/$', upload, name='upload'),
    url(r'^(?P<slug>[\w\-]+)/$', poc_detail, name='nutr_poc_detail'),
    url(r'^(?P<poc_slug>[\w\-]+)/' r'add_article_link/$', NewsLinkCreate.as_view(), name='nutr_newslink_create'),
    url(r'^(?P<slug>[\w\-]+)/delete/$', POCDelete.as_view(), name='nutr_poc_delete'),
    url(r'^(?P<slug>[\w\-]+)/update/$', POCUpdate.as_view(), name='nutr_poc_update'),
    url(r'^(?P<poc_slug>[\w\-]+)/' r'(?P<newslink_slug>[\w\-]+)/' r'delete/$', NewsLinkDelete.as_view(), name='nutr_newslink_delete'),
    url(r'^(?P<poc_slug>[\w\-]+)/' r'(?P<newslink_slug>[\w\-]+)/' r'update/$', NewsLinkUpdate.as_view(), name='nutr_newslink_update'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

