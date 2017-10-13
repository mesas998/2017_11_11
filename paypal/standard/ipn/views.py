#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging

from django.http import HttpResponse, QueryDict
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from paypal.standard.ipn.forms import PayPalIPNForm
from paypal.standard.ipn.forms2 import PayPalPaymentsForm, SalePaymentForm
from paypal.standard.ipn.models import PayPalIPN
from paypal.standard.models import DEFAULT_ENCODING
from paypal.utils import warn_untested
from django.views.generic import View
from django.shortcuts import get_object_or_404, redirect, render, render_to_response
from django.core.urlresolvers import reverse, reverse_lazy
from django.template import RequestContext

logger = logging.getLogger(__name__)

CONTENT_TYPE_ERROR = ("Invalid Content-Type - PayPal is only expected to use "
                      "application/x-www-form-urlencoded. If using django's "
                      "test Client, set `content_type` explicitly")
def charge(request):
    print('charge() 23d')
 
    if request.method == "POST":
        print('charge() 23g - request.POST is a ',type(request.POST))
        print('charge() 23h - request.POST.items(): ',request.POST.items())
        for x in list(request.POST.items()):
            print ('charge() 23i: ', x)
        for k,v in list(request.POST.items()):
            print ('charge() 23j: ', k,':',v)
        #orm = PayPalPaymentsForm(request.POST)
        form = SalePaymentForm(request.POST)
        print('charge() 23m')
        #oken = request.POST['stripeToken']
        print('charge() 23n')
 
        if form.is_valid(): # charges the card
            print('charge() 23p')
            return HttpResponse("{% url nutr_tag_list %}")
            #eturn render( request, 'nutr/tag_list.html', {'tag_list': Tag.objects.all()})
            print('charge() 23q')
    else:
        print('charge() 23r')
        #orm = PayPalPaymentsForm()
        form = SalePaymentForm()
        print('charge() 23s')
 
    return render_to_response("ipn/payment7.html", RequestContext( request, {'form': form} ) )
    #eturn render_to_response("ipn/payment.html", RequestContext( request, {'form': form} ) )
    #eturn render_to_response("ipn/paypal_pasted.html", RequestContext( request, {'form': form} ) )
    """
    #django-paypal:
    print("charge() 24b")
    try:
        paypal_dict = {
            "business": "receiver_email@example.com",
            "amount": "10000000.00",
            "item_name": "name of the item",
            "invoice": "unique-invoice-id",
            "custom": "premium_plan",  # Custom command to correlate to some function later (optional)
        }
    except Error as e:
        print("charge() 24d: ",e)
    print('charge() 24f: ',type(paypal_dict))
    #notify_url": request.build_absolute_uri(reverse('paypal-ipn')),
    #return_url": request.build_absolute_uri(reverse('your-return-view')),
    #cancel_return": request.build_absolute_uri(reverse('your-cancel-view')),

    # Create the instance.
    form = PayPalPaymentsForm(initial=paypal_dict)
    print('charge() 24m')
    context = {"form": form}
    print('charge() 24p')
    return render(request, "sales/payment.html", context)
    """ 


def view_that_asks_for_money(request):
    # What you want the button to do.
    print('view_that_asks_for_money() 44b')
    paypal_dict = {
        "card":"",
        "business": "receiver_email@example.com",
        "amount": "10000000.00",
        "item_name": "name of the item",
        "invoice": "unique-invoice-id",
        "notify_url": request.build_absolute_uri(reverse('paypal_url_name')),
        "return_url": request.build_absolute_uri(reverse('nutr_tag_list')),
        "cancel_return": request.build_absolute_uri(reverse('nutr_tag_list')),
        "custom": "premium_plan",  # Custom command to correlate to some function later (optional)
    }
    print('view_that_asks_for_money() 44g')
    # Create the instance.
    form = PayPalPaymentsForm(initial=paypal_dict)
    print('view_that_asks_for_money() 44m')
    context = {"form": form}
    print('view_that_asks_for_money() 44p')
    return render(request, "ipn/payment.html", context)
 
class Test(View):
    def post():
        pass

def test(request):
    print('ipn() 41c')
    return HttpResponse("OKAY")

#require_POST
#csrf_exempt
def testtt(request):
    print('ipn() 40c')
    pass
    """
    PayPal IPN endpoint (notify_url).
    Used by both PayPal Payments Pro and Payments Standard to confirm transactions.
    http://tinyurl.com/d9vu9d

    PayPal IPN Simulator:
    https://developer.paypal.com/cgi-bin/devscr?cmd=_ipn-link-session
    """
    # TODO: Clean up code so that we don't need to set None here and have a lot
    #       of if checks just to determine if flag is set.
    flag = None
    ipn_obj = None
    print('ipn() 40e: ',request.META.get('CONTENT_TYPE', ''))

    # Avoid the RawPostDataException. See original issue for details:
    # https://github.com/spookylukey/django-paypal/issues/79
    """ 
    commented
    PayPal is only expected to use application/x-www-form-urlencoded. 
    If using django's test Client, set `content_type` explicitly   
    if not request.META.get('CONTENT_TYPE', '').startswith(
            'application/x-www-form-urlencoded'):
        raise AssertionError(CONTENT_TYPE_ERROR)
    """
    print('ipn() 40g')

    logger.debug("PayPal incoming POST data: %s", request.body)

    # Clean up the data as PayPal sends some weird values such as "N/A"
    # Also, need to cope with custom encoding, which is stored in the body (!).
    # Assuming the tolerant parsing of QueryDict and an ASCII-like encoding,
    # such as windows-1252, latin1 or UTF8, the following will work:
    encoding = request.POST.get('charset', None)

    encoding_missing = encoding is None
    if encoding_missing:
        encoding = DEFAULT_ENCODING

    print('ipn() 40m')
    try:
        data = QueryDict(request.body, encoding=encoding).copy()
    except LookupError:
        warn_untested()
        data = None
        flag = "Invalid form - invalid charset"

    if data is not None:
        if hasattr(PayPalIPN._meta, 'get_fields'):
            date_fields = [f.attname for f in PayPalIPN._meta.get_fields() if f.__class__.__name__ == 'DateTimeField']
        else:
            date_fields = [f.attname for f, m in PayPalIPN._meta.get_fields_with_model()
                           if f.__class__.__name__ == 'DateTimeField']

        for date_field in date_fields:
            if data.get(date_field) == 'N/A':
                del data[date_field]

        print('ipn() 40o: ',type(data))
        for key in data:
          print('ipn() 40q ',key,':',data[key])
        form = PayPalIPNForm(data)
        context = {"form": form}
        template_name = 'ipn/ipn.html'
        return render(request, template_name, context)

        print('ipn() 40q1: ',type(form))
        if form.is_valid():
            print('ipn() 40q2')
            try:
                # When commit = False, object is returned without saving to DB.
                ipn_obj = form.save(commit=False)
                print('ipn() 40q3')
            except Exception as e:
                flag = "Exception while processing. (%s)" % e
        else:
            formatted_form_errors = ["{0}: {1}".format(k, ", ".join(v)) for k, v in form.errors.items()]
            flag = "Invalid form. ({0})".format(", ".join(formatted_form_errors))
    print('ipn() 40r')

    if ipn_obj is None:
        ipn_obj = PayPalIPN()
        print('ipn() 40q5: ',ipn_obj)

    # Set query params and sender's IP address
    ipn_obj.initialize(request)
    print('ipn() 40u')

    if flag is not None:
        # We save errors in the flag field
        ipn_obj.set_flag(flag)
    else:
        # Secrets should only be used over SSL.
        if request.is_secure() and 'secret' in request.GET:
            print('ipn() 40v')
            warn_untested()
            ipn_obj.verify_secret(form, request.GET['secret'])
        else:
            print('ipn() 40w')
            ipn_obj.verify()

    print('ipn() 40x')
    ipn_obj.save()
    ipn_obj.send_signals()

    if encoding_missing:
        # Wait until we have an ID to log warning
        logger.warning("No charset passed with PayPalIPN: %s. Guessing %s", ipn_obj.id, encoding)
    print('ipn() 40y')

    return HttpResponse("OKAY")
