from django import forms
from django.forms.widgets import PasswordInput
class LoginForm(forms.Form):
    number = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
