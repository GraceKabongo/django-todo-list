from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from .form import UserForm, UserRegistrationForm


def sign_in(request):
    form = UserForm()
        
    if request.method == "POST":
        username = request.POST['username']
        password =  request.POST['password']
        user = authenticate(
    		    request, 
    		    username=username, 
    		    password=password
        )
        if user is None:
            return HttpResponse("Invalid credentials.")
        
        login(request, user)
        return redirect('home')
    else:
        return render(request, 'login.html', {'form' : form})


def sign_out(request):
    logout(request)
    return redirect('/')


            
def sign_up(request):
    
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        new_user = User.objects.create_user(
        	username=username,
        	password=password,
        	email=email
        )
        try:
            new_user.save()
            login(request, new_user)
            return redirect('home')
        except:
            return HttpResponse("Something went wrong.") 
    else:
        form = UserRegistrationForm()
    return render(request, template_name='register.html', context={'form' : form})