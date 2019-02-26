from django.http import HttpResponse
from django.shortcuts import render
from .forms import SignupForm,LoginForm

def signUp(request):
    if request.method == 'POST':
        form_response=SignupForm(request.POST)
        if form_response.is_valid():
            name=form_response.cleaned_data.get("name")
            email = form_response.cleaned_data.get ("email")
            password = form_response.cleaned_data.get ('password')
            print(name,email,password)
        else:
            print("Invalid Response")
    else:
        print("Not a Post Request")

    form_response = SignupForm
    return render(request,'Signup.html',{'form':SignupForm})

def logIn(request):
    if request.method == 'POST':
        form_response=LoginForm(request.POST)
        if form_response.is_valid():
            email = form_response.cleaned_data.get ("email")
            password = form_response.cleaned_data.get ('password')
            print(email,password)
        else:
            print("Invalid Response")
    else:
        print("Not a Post Request")

    form_response = LoginForm
    return render(request,'login.html',{'form':LoginForm})