from django.conf.urls import url
from ..views import POCList, poc_detail, image
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^(?P<jpg>[\w\-]+).jpg$', image, name='nutr_image'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
