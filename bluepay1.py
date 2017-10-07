##
# BluePay Python Sample code.
#
# This code sample runs a $3.00 CC Sale transaction
# against a customer using test payment information.
##
from __future__ import print_function
import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
from BluePay import BluePay

account_id = "100484421537"
secret_key = "IlqHucuI"
mode = "TEST"  

payment = BluePay(
    account_id = account_id, 
    secret_key = secret_key, 
    mode = mode
) 
print ("payment created")

payment.set_customer_information(
    name1 = "Bob",
    name2 = "Tester",
    addr1 = "123 Test St.",
    addr2 = "Apt #500",
    city = "Testville",
    state = "IL",
    zipcode = "54321",
    country = "USA"
)
print ("customer info set")

payment.set_cc_information(
    card_number = "4111111111111111",
    card_expire = "1220",
    cvv2 = "123"    
)
print ("cc info set")

payment.sale(amount = '3.00') # Sale Amount: $3.00
print ("payment sale() fired")

# Makes the API Request
payment.process()
print ("payment process() fired")

# Read response from BluePay
if payment.is_successful_response():
    print('Transaction Status: ' + payment.status_response)
    print('Transaction Message: ' + payment.message_response)
    print('Transaction ID: ' + payment.trans_id_response)
    print('AVS Result: ' + payment.avs_code_response)
    print('CVV2 Result: ' + payment.cvv2_code_response)
    print('Masked Payment Account: ' + payment.masked_account_response)
    print('Card Type: ' + payment.card_type_response)
    print('Auth Code: ' + payment.auth_code_response)
else:
    print(payment.message_response)

