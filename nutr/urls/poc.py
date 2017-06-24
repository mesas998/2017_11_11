from django.conf.urls import url
from ..views import POCList, poc_detail
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^$', POCList.as_view(), name='nutr_poc_list'),
    url(r'^(?P<pk>[\w\-]+)/$', poc_detail, name='nutr_poc_detail'),
    #rl(r'^create/$', EPAColoCreate.as_view(), name='nutr_epacolo_create'),
    #rl(r'^(?P<slug>[\w\-]+)/delete/$', EPAColoDelete.as_view(), name='nutr_epacolo_delete'),
    #rl(r'^(?P<slug>[\w\-]+)/update/$', EPAColoUpdate.as_view(), name='nutr_epacolo_update'),
    #rl(r'^(?P<slug>[\w]+)/$', EPAColoDetail.as_view(), name='nutr_epacolo_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
