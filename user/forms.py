import logging

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import \
    UserCreationForm as BaseUserCreationForm

from .utils import ActivationMailFormMixin
from sendgrid import sendgrid
import os
import sendgrid
from sendgrid.helpers.mail import *
logger = logging.getLogger(__name__)


class ResendActivationEmailForm(
        ActivationMailFormMixin, forms.Form):

    email = forms.EmailField()

    mail_validation_error = (
        'Could not re-send activation email. '
        'Please try again later. (Sorry!)')

    def save(self, **kwargs):
        User = get_user_model()
        try:
            user = User.objects.get(
                email=self.cleaned_data['email'])
        except:
            logger.warning(
                'Resend Activation: No user with '
                'email: {} .'.format(
                    self.cleaned_data['email']))
            return None
        self.send_mail(user=user, **kwargs)
        return user


class UserCreationForm(
        ActivationMailFormMixin,
        BaseUserCreationForm):

    mail_validation_error = (
        'User created. Could not send activation '
        'email. Please try again later. (Sorry!)')

    class Meta(BaseUserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email')

    def save(self, **kwargs):
        print('UserCreationForm (41)')
        user = super().save(commit=False)
        print('UserCreationForm (42) - user: ',user)
        print('UserCreationForm (42) - user.pk: ',user.pk)
        if not user.pk:
            print('UserCreationForm (43) ')
            #ser.is_active = False
            user.is_active = True 
            send_mail = True
        else:
            print('UserCreationForm (44) ')
            send_mail = False
        print('UserCreationForm (44a) ')
        user.save()
        print('UserCreationForm (44b) ')
        self.save_m2m()
        print('UserCreationForm (44c) ')
        if send_mail:
            print('UserCreationForm (45) ')
            self.send_mail(user=user, **kwargs) #this is returning False
            print('UserCreationForm (46)')
            #elf.sendgrid()
        return user

    def sendgrid(self, **kwargs):
        SENDGRID_API_KEY=      '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'
        SENDGRID_PASSWORD=     'pjamfoyy0286'
        SENDGRID_USERNAME=     'app73564228@heroku.com'
        print('UserCreationForm (51)')
        sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
        print('UserCreationForm (51a')
        from_email = Email("michael.sweeney303@gmail.com")
        print('UserCreationForm (51b')
        subject = "Hello World from the SendGrid Python Library!"
        print('UserCreationForm (51c')
        to_email = Email("michael.sweeney303@gmail.com")
        content = Content("text/plain", "Hello, Email!")
        mail = Mail(from_email, subject, to_email, content)
        print('UserCreationForm (51d')
        response = sg.client.mail.send.post(request_body=mail.get())
        print('UserCreationForm (51e')
        print(response.status_code)
        print(response.body)
        print(response.headers)
