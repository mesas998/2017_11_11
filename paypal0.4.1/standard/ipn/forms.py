#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from paypal.standard.forms import PayPalStandardBaseForm
from paypal.standard.ipn.models import PayPalIPN
from django import forms


class PayPalIPNForm(PayPalStandardBaseForm):
    """
    Form used to receive and record PayPal IPN notifications.

    PayPal IPN test tool:
    https://developer.paypal.com/us/cgi-bin/devscr?cmd=_tools-session
    """

    class Meta:
        model = PayPalIPN
        exclude = []


