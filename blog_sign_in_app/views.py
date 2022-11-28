from django.http import HttpResponse
from django.shortcuts import render,redirect
from blog_sign_in_app.forms import User,custom_reg
from blogapp.models import post
# Create your views here.
def signin(request):
    if request.method == 'POST':
        regform = custom_reg(request.POST)
        if regform.is_valid():
            regform.save()
            return redirect("login")
            
    else:
        regform=custom_reg()
    return render(request,'signin.html',{'regform':regform})


def login(request):
    return render(request,'login.html')

def logout(request):
    return render (request,'logout.html')


def profile(request):
    return render (request,'profile.html')
    