from django.http import HttpResponse
from django.shortcuts import render
from .forms import SignupForm

def signUp(request):
    if request.method == 'POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            firstName = form.cleaned_data['fname']
            lastName = form.cleaned_data['lname']
            gender = form.cleaned_data['gender']
            email = form.cleaned_data['email']
            bday = form.cleaned_data['bday']
            print(firstName,lastName,gender,email,bday)
        else:
            print("invalid ")

    form = SignupForm

    return render(request,'Signup.html',{'form':SignupForm})

