from django.http import HttpResponse
from django.shortcuts import render
from .forms import signUpForm, LoginForm



def signUpFormDetail(request):
    if request.method == 'POST':
        form_response=signUpForm(request.POST)
        if form_response.is_valid():
            form_response.save()


    form_response = signUpForm()
    return render(request,'Signup.html',{'form':signUpForm})










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