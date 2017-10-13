from __future__ import unicode_literals

from django.conf.urls import url

#rom paypal.standard.ipn import views
#mport views
#rom .views import testtt
from .views import Test, testtt, view_that_asks_for_money, charge

urlpatterns = [
    #rl(r'^$', charge, name="paypal_url_name"),
    url(r'^$', view_that_asks_for_money, name="paypal_url_name"),
    #rl(r'^$', testtt, name="paypal_url_name"),
    #rl(r'^$', POCList.as_view(), name='nutr_poc_list'),
]
