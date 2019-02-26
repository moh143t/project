from django import forms


class SignupForm(forms.Form):
    firstName=forms.CharField(widget=forms.TextInput(),required=True,max_length=50)
    lastName=forms.CharField(widget=forms.TextInput(),required=True,max_length=50)
    gender=forms.ChoiceField(choices=[('male','Male'),('female','Female')])
    email=forms.EmailField(widget=forms.TextInput(),required=True)
    bday=forms.DateField(widget=forms.DateInput())


