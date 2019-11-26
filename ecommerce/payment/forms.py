
from django import forms

from .models import Payment

import getpass

print(getpass.getuser())


class PaymentForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    phone_no = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Phone Number'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Address'}))
    state = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'State'}))
    city = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'City'}))

    class Meta:
        model = Payment
        fields = ['first_name', 'last_name',  'phone_no', 'address', 'state', 'city']


class CardForm(forms.ModelForm):
    card_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Card Name'}), label='')
    card_number = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Card Number'}), label='')
    expiring_month = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Month'}), label='')
    expiring_year = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Year'}), label='')
    card_cvv = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'cvv'}), label='')

    class Meta:
        model = Payment
        fields = ['card_name', 'card_number', 'expiring_month', 'expiring_year', 'card_cvv']