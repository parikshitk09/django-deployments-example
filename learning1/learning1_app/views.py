from django.shortcuts import render

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from learning1_app.forms import UserInfoForm

# Create your views here.

def about(request):
    return render(request,'main_app/about.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
    
def index(request):
    return render(request,'main_app/base.html')

def register(request):
    registered = False

    if request.method == 'POST':

        user_form = UserInfoForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserInfoForm()

    return render(request,'main_app/register.html',{'user_form':user_form,'registered':registered})

def user_login(request):

    if request.method =='POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:

            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse("Your account is not active")

        else:
            return HttpResponse("Invalid User login")

    else:
        return render(request,'main_app/logged_in.html',{})
