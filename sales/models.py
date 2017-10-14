from django.db import models
from django.conf import settings
import os
from inspect import signature
 
class Sale(models.Model):
    def __init__(self, *args, **kwargs):
        super(Sale, self).__init__(*args, **kwargs)
 
        # bring in stripe, and get the api key from settings.py
        import stripe
        #tripe.api_key = settings.STRIPE_API_KEY
        stripe.api_key = os.environ.get("STRIPE_API_KEY")
 
        self.stripe = stripe
        print('charge() 32a - self.stripe: ',self.stripe)
 
    # store the stripe charge id for this sale
    charge_id = models.CharField(max_length=32)
 
    # you could also store other information about the sale
    # but I'll leave that to you!
 
    #ef charge(self, request, email, fee):
    #ef charge(self, price_in_cents, number, exp_month, exp_year, cvc):
    def whatever(self, price_in_cents, number, exp_month, exp_year, cvc):
        print('charge() 55a0 - self.stripe.version: ',self.stripe.version)
        if self.charge_id: # don't let this be charged twice!
            return False, Exception(message="Already charged.")
 
        try:
            print('charge() 55b0 - self.stripe.version: ',self.stripe.version)
            response = self.stripe.Charge.create(
                amount = price_in_cents,
                currency = "usd",
                card = {
                    "number" : number,
                    "exp_month" : exp_month,
                    "exp_year" : exp_year,
                    "cvc" : cvc,
                },
                description='Thank you for your donation!')
 
            self.charge_id = response.id
            print('charge() 55b1 - self.stripe.version: ',self.stripe.version)
 
        except self.stripe.CardError as ce:
            print('charge() 55b2 - self.stripe.version: ',self.stripe.version)
            # charge failed
            return False, ce
        return True, response

    def nameerror(self, amount, token):
        # Set your secret key: remember to change this to your live secret key
        # in production. See your keys here https://manage.stripe.com/account
        print('charge() 32b0 - self.stripe.version: ',self.stripe.version)
        print('charge() 32b1 - type(self.stripe): ',type(self.stripe))
        #rint('charge() 32b2 - self.stripe.__dict__: ',self.stripe.__dict__)
        print('charge() 32b3 - type(self.stripe.__dict__): ',type(self.stripe.__dict__))
        # no go (?):
        #or k,v in self.stripe.__dict__:
            #rint('charge() 32b4 ',k,':',v)
  
        print('charge() 32c - amount: ',amount)
        print('charge() 32c - type(amount): ',type(amount))
        print('charge() 32c - number: (omitted)')
        print('charge() 32c - token: ',token)
        print('charge() 32c - type(token): ',type(token))
        print('charge() 32c - self.stripe.api_key: ',self.stripe.api_key)
        #tripe.api_key = settings.STRIPE_SECRET_KEY
        #tripe_customer = stripe.Customer.create( card=token, description="donation")
        print('charge() 32e')
        # Get the credit card details submitted by the form
        #tripe_customer = None
        try:
            #oken = request.POST['stripeToken']
            #tripe_customer = stripe.Customer.create( card=token, description='donation')
            print('charge() 32f1 - self.stripe.__dict__: ',self.stripe.__dict__)
            print('charge() 32f1 - self.stripe: ',self.stripe)
            print('charge() 32f2 - self.stripe.Charge: ',self.stripe.Charge)
            print('charge() 32f3 - self.stripe.Charge.__dict__: ',self.stripe.Charge.__dict__)
            print('charge() 32f4 - dir(self.stripe.Charge): ',dir(self.stripe.Charge))
            print('charge() 32f5 - signature(self.stripe.Charge.serialize): ',signature(self.stripe.Charge.serialize))
            #create():  (api_key=None, idempotency_key=None, stripe_version=None, stripe_account=None, **params)
            #tripe.Charge.retrieve( "ch_1BCbWBGlXetMXVEdcJFB0SJB", self.api_key)
            print('charge() 32f6')
            #tripe.Charge.retrieve( source=token, amount=int(100*amount))
            #tripe.Charge.clear()
            customer = stripe.Customer.create( email="paying.user@example.com", source=token,)
            #harge = stripe.Charge.create( amount=1000, currency="usd", customer=customer.id,)

            print('charge() 32f7')
            #harge = stripe.Charge.create( amount=1000, currency="usd", description="Example charge", source=token,) 
            print('charge() 32f8')
            #elf.stripe.Charge.charge()
            #harge = stripe.Charge.create( amount=1000, currency="usd", source=token, description="Example charge")
            #hat=self.stripe.Charge.create(api_key=None, idempotency_key=None, stripe_version=None, stripe_account=None, **params)
            #hat=self.stripe.Charge.create( amount=int(100*amount), currency="usd", customer=stripe_customer.id)
            print('charge() 32g3 ')
        except:
            print('charge() 32h: ',sys.exc_info()[0])
        #rint('charge() 32l - stripe_customer: ',type(stripe_customer))
        # Save the Stripe ID to the customer's profile
        #elf.stripe_id = stripe_customer.id
        #rint('charge() 32n')
        #elf.save()
        print('charge() 32p')

        """
        # Charge the Customer instead of the card
        stripe.Charge.create(
            amount=fee, # in cents
            currency="usd",
            customer=stripe_customer.id
        )
        """
        print('charge() 32t')
        #eturn stripe_customer
        return None
        print('charge() 32w')

    def charge(self, price_in_cents, number, exp_month, exp_year, cvc):
        """
        Takes a the price and credit card details: number, exp_month,
        exp_year, cvc.
 
        Returns a tuple: (Boolean, Class) where the boolean is if
        the charge was successful, and the class is response (or error)
        instance.
        """
        print('charge() 31c')
 
        if self.charge_id: # don't let this be charged twice!
            print('charge() 31e')
            return False, Exception(message="Already charged.")
 
        try:
            print('charge() 31g - price_in_cents: ',price_in_cents)
            print('charge() 31g - number        : ',number)
            print('charge() 31g - exp_month     : ',exp_month)
            print('charge() 31g - exp_year      : ',exp_year)
            print('charge() 31g - cvc:            ',cvc)
            response = self.stripe.Charge.create( #should create token I'm told (?)
            #esponse = self.stripe.card.createToken(
                amount = price_in_cents,
                currency = "usd",
                card = {
                    "number" : number,
                    "exp_month" : exp_month,
                    "exp_year" : exp_year,
                    "cvc" : cvc,
 
                    #### it is recommended to include the address!
                    #"address_line1" : self.address1,
                    #"address_line2" : self.address2,
                    #"daddress_zip" : self.zip_code,
                    #"address_state" : self.state,
                },
                description='Thank you for your purchase!')
 
            print('charge() 31m')
            self.charge_id = response.id
            print('charge() 31p')
 
        except self.stripe.CardError as ce:
            # charge failed
            print('charge() 31s - self.stripe.CardError: ',ce)
            return False, ce
        except Error as e:
            # charge failed
            print('charge() 31u: ',e)
            return False, ce
 
        return True, response

        """
                card = {
                    "number" : number,
                    "exp_month" : exp_month,
                    "exp_year" : exp_year,
                    "cvc" : cvc,
 
                    #### it is recommended to include the address!
                    #"address_line1" : self.address1,
                    #"address_line2" : self.address2,
                    #"daddress_zip" : self.zip_code,
                    #"address_state" : self.state,
                },
        """
