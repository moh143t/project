
from django.contrib import admin
from django.urls import  path
from . import views


urlpatterns = [

    path('', views.signUpFormDetail),
    path('login',views.logIn),
]
