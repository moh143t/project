from django import forms


class SignupForm(forms.Form):
    name= forms.CharField(label="Name",required=True)
    email = forms.EmailField (label="Email Address",required=True)
    password = forms.CharField (widget=forms.PasswordInput,required=True)
    password2 = forms.CharField (widget=forms.PasswordInput, label="Confirm Password",required=True)


class LoginForm(forms.Form):
    email = forms.EmailField (label="Email Address", required=True)
    password = forms.CharField (widget=forms.PasswordInput, required=True)