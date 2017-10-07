#!/usr/local/bin/python
import stripe
import sys
stripe.api_key  = 'sk_test_bBEFBc07pwFkpHdOSO1ev1Oi'
if stripe.VERSION in ("1.13.0", "1.14.0", "1.14.1", "1.15.1", "1.16.0", "1.17.0", "1.18.0", "1.19.0"):
  print ("Bindings update required.")

"""
stripe.Charge.all()
#stripeCustomer = stripe.Customer.create() 
print ("TLS 1.2 supported, no action required.")
try:
  stripe.Charge.all()
  print ("TLS 1.2 supported, no action required.")
except stripe.error.APIConnectionError:
  print ("APIConnectionError")
except:
  print ("Unexpected error:", sys.exc_info()[0])
  raise
"""

print ("attempting create")

resp = stripe.Charge.create(
    amount=200,
    currency='usd',
    card='tok_visa',
    description='customer@gmail.com'
)

print ('Success: %r' % (resp, ))
