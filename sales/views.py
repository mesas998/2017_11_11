from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from django.core.urlresolvers import reverse
from paypal.standard.forms import PayPalPaymentsForm
 
from sales.models import Sale
from sales.forms import SalePaymentForm
 
def charge(request):
    print('charge() 23d')
 
    #stripe:
    if request.method == "POST":
        print('charge() 23g')
        form = SalePaymentForm(request.POST)
        print('charge() 23m')
 
        if form.is_valid(): # charges the card
            print('charge() 23p')
            return HttpResponse("Success! We've charged your card!")
    else:
        form = SalePaymentForm()
        print('charge() 23s')
 
    return render_to_response("sales/charge.html", RequestContext( request, {'form': form} ) )
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
