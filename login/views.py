from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django import forms
from django.contrib.auth.models import User
from .register_forms import RegisterForm
from .login_forms import LoginForm
# Create your views here.

def home(request):
    return render(request,"home/home.html")

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            import pdb; pdb.set_trace()
            username = userObj['username']
            email =  userObj['email']
            password =  userObj['password']
            if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                pdb.set_trace()
                User.objects.create_user(username, email, password)
                user = authenticate(username = username, password = password)
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                raise forms.ValidationError('Looks like a username with that email or password already exists')
    else:
        form = RegisterForm()
    return render(request, 'home/register.html', {'form' : form})

def logins(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            import pdb; pdb.set_trace()
            userObj = form.cleaned_data
            username = userObj['username']
            password =  userObj['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                raise forms.ValidationError('Looks like a username with that email or username already exist')
    else:
        form = LoginForm()
    return render(request, 'home/login.html', {'form' : form})
