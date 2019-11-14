

from django import forms
from django.forms import fields

class Autn(forms.Form):
    username = fields.CharField(max_length=18,required=True,label='username')
    password = fields.CharField(widget=forms.PasswordInput,label='password')
