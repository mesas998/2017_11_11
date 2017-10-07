from django.conf.urls import url
from .views import charge
 
urlpatterns = [
    url(r'^charge/$', charge, name="charge"),
]
