from sendgrid import sendgrid
import os
from sendgrid.helpers.mail import *

#########################################################################################################
# first do  this:
# $ export SENDGRID_API_KEY=SG.FVzPxg0ZSeu8Fw9ccT1e0Aexport.9hYUbT6REiE5Ug2g2Nk2A4PsVVLr91MmQjvxQiiSwr  #
#########################################################################################################
#g = sendgrid.SendGridAPIClient(apikey=os.environ.get('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'))
#g = sendgrid.SendGridAPIClient('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')
sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
from_email = Email("michael.sweeney303@gmail.com")
subject = "Hello World from the SendGrid Python Library!"
to_email = Email("michael.sweeney303@gmail.com")
content = Content("text/plain", "Hello, Email!")
mail = Mail(from_email, subject, to_email, content)
response = sg.client.mail.send.post(request_body=mail.get())
print(response.status_code)
print(response.body)
print(response.headers)

