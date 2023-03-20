from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django_otp.forms import OTPAuthenticationForm

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Username',
                               widget=forms.TextInput(attrs={'class': 'form-control', 'autocomplete': "on"}))

    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'autocomplete': "off"}))

    # otp_device = forms.CharField(required=False, widget=forms.Select)

    otp_token = forms.CharField(label='Token',
                                widget=forms.TextInput(attrs={'class': 'form-control', 'autocomplete': "off"}))

    # otp_challenge = forms.CharField(required=False)