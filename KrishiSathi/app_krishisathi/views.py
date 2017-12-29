from django.shortcuts import render, HttpResponse, redirect
from .models import User_Info, User_Data
from django.contrib.auth.hashers import make_password
from django import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

#For the REST API:
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import User_DataSerializer, User_InfoSerializer

# Create your views here.
def show_homepage(request):
    return render(request, 'app_krishisathi/index.html')

def show_signup(request):
    registered_status = False

    if request.POST:
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        username = request.POST.get('username')
        devicecode = request.POST.get('devicecode')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirmation = request.POST.get('password_confirmation')
        if(password == password_confirmation):
            password = make_password(password)
        else:
            raise forms.ValidationError("Passwords do not match")
        gender = request.POST.get('gender')
        country = request.POST.get('country')
        user_data = User(first_name=fname,last_name=lname,username=username,email=email,password=password)
        user_data.save()
        user_info_data = User_Info(gender=gender,country=country,devicecode=devicecode)
        user_info_data.user = user_data
        user_info_data.save()
        registered_status = True

    context = {'registered_status':registered_status}
    return render(request, 'app_krishisathi/signup_form.html', context)

def show_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        # For authentication, you don't need to covert the password into hash
        #         #This is done automatically by django at the backend
        #         #Authenticating the entered user's credentials
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                #To get a User with the given username
                user_info = User.objects.get(username=username)
                #To get all data from User_Info containing a user having username=username
                user_details = User_Info.objects.get(user__username=username)

                devicecode = user_details.devicecode
                user_data = User_Data.objects.filter(devicecode=devicecode)
                context = {'user':user,
                           'user_info': user_info,
                           'user_details': user_details,
                           'user_data': user_data,}
                return render(request, 'app_krishisathi/user_profile.html', context)
            else:
                return HttpResponse("<h1>Oops! Your account has not been active for a while now!</h1>")
        else:
            return HttpResponse(username+" "+make_password(password)+" <h1>User NOT FOUND!!</h1>")
    else:
        return render(request, 'app_krishisathi/login_form.html')


@login_required
def user_logout(request):
    logout(request)
    return redirect('login')


def show_aboutpage(request):
    return render(request, 'app_krishisathi/about.html')

def show_contactpage(request):
    return render(request, 'app_krishisathi/contact.html')


class User_DataList(APIView):

    def get(self, request):
        all_data = User_Data.objects.all()
        serializer = User_DataSerializer(all_data, many=True)
        return Response(serializer.data)

    def post(self, request):
        pass

class User_InfoList(APIView):

    def get(self, request):
        all_info = User_Info.objects.all()
        serializer = User_InfoSerializer(all_info, many=True)
        return Response(serializer.data)

    def post(self, request):
        pass
