from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages

from krishiapp.models import UserProfile, UserReadings


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
            return redirect('profile', user.id)
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
                return redirect('profile', user.id)
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


def profile(request, id):
    readings = UserReadings.objects.filter(user_id=id).values('ph', 'temp', 'moisture', 'humidity', 'datetime')
    ph_readings = []
    temp_readings = []
    moisture_readings = []
    humidity_readings = []
    datetimes = []
    for reading in readings:
        ph_readings.append(reading.get('ph'))
        temp_readings.append(reading.get('temp'))
        moisture_readings.append(reading.get('moisture'))
        humidity_readings.append(reading.get('humidity'))
        datetimes.append(reading.get('datetime').isoformat())
    print(ph_readings, datetimes)
    context = {
        'ph_readings': ph_readings,
        'temp_readings': temp_readings,
        'moisture_readings': moisture_readings,
        'humidity_readings': humidity_readings,
        'datetimes': datetimes
    }
    return render(request, 'profile.html', context)


def api_add_readings(request):
    try:
        UserReadings.objects.create(user_id=request.GET.get('user_id'),
                                    ph=request.GET.get('ph'),
                                    humidity=request.GET.get('humidity'),
                                    moisture=request.GET.get('moisture'),
                                    temp=request.GET.get('temp'),
                                    datetime=request.GET.get('datetime'))
        return JsonResponse({'success': True}, safe=False)

    except Exception as error:
        return JsonResponse({'success': False}, safe=False)


