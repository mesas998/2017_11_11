from django.conf.urls import url

from ..views import tag_detail
from ..views import TagList, TagCreate, TagUpdate, TagDelete

urlpatterns = [
    #rl(r'^$', tag_list, name='nutr_tag_list'),
    url(r'^$', TagList.as_view(), name='nutr_tag_list'),
    url(r'^create/$', TagCreate.as_view(), name='nutr_tag_create'),
    url(r'^(?P<slug>[\w\-]+)/$', tag_detail, name='nutr_tag_detail'),
    url(r'^(?P<slug>[\w-]+)/delete/$', TagDelete.as_view(), name='nutr_tag_delete'),
    url(r'^(?P<slug>[\w\-]+)/update/$', TagUpdate.as_view(), name='nutr_tag_update'),
]
