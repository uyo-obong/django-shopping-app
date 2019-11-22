from django import forms
from .models import Contact
from django.contrib.auth.models import User


class ContactForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your Name'}), label='')
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Your Email'}), label='')
    phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your Phone Number'}), label='')
    description = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Your Name', 'rows': 5
    }), label='')

    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'description']


class RegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=50)
    first_name = forms.CharField(max_length=40)
    last_name = forms.CharField(max_length=40)
    email = forms.EmailField()
    password = forms.CharField(min_length=3, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
