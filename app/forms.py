from django import forms
from .models import signUp


class signUpForm(forms.ModelForm):
    name = forms.CharField(label="Name", required=True)
    email = forms.EmailField(label="Email Address", required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    class Meta:
        model = signUp
        fields=('name','email','password')


class LoginForm(forms.Form):
    email = forms.EmailField (label="Email Address", required=True)
    password = forms.CharField (widget=forms.PasswordInput, required=True)