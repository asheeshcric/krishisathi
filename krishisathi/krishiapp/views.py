from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages

from krishiapp.models import UserProfile


# Create your views here.

def homepage(request):
    return render(request, 'homepage.html')


def signup(request):
    if request.method == 'POST':
        try:
            user = User.objects.create_user(username=request.POST.get('username'),
                                            email=request.POST.get('email'),
                                            password=request.POST.get('password'),
                                            first_name=request.POST.get('first_name'),
                                            last_name=request.POST.get('last_name'),
                                            is_superuser=0, is_active=1)
            UserProfile.objects.create(user=user, address=request.POST.get('address'),
                                       contact=request.POST.get('contact'))
            login_user = authenticate(request, username=user.username, password=request.POST.get('password'))
            login(request, login_user)
            messages.success(request, 'User created successfully.')
            return redirect('profile')
        except Exception as error:
            print(error)
            messages.error(request, 'User creation failed. Please try again.')
    return render(request, 'signup.html')


def login_user(request):
    if request.method == 'POST':
        try:
            user = authenticate(request, username=request.POST.get('username'), password=request.POST.get('password'))
            if user:
                login(request, user)
                messages.success(request, 'Login Successful.')
                return redirect('profile')
            else:
                messages.error(request, 'Please enter correct username and password.')
        except Exception as error:
            messages.error(request, 'Something went wrong. Please try again.')

    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    messages.error(request, 'Logged out successfully.')
    return redirect('homepage')


def about(request):
    return render(request, 'about.html')


def profile(request):
    return render(request, 'profile.html')
