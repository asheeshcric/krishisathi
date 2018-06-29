from django.shortcuts import render

# Create your views here.


def homepage(request):
    return render(request, 'homepage.html')

def signup(request):
    return render(request, 'signup.html')

def login(request):
    return render(request, 'login.html')

def about(request):
    return render(request, 'about.html')