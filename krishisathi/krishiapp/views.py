from collections import Counter

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone

from krishiapp.models import UserProfile, UserReadings
from .machine_learning.machine_learning import test_model


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
    if not request.user.is_authenticated:
        messages.error(request, "Please log in to access your profile.")
        return redirect('login')
    user_id = request.user.id
    readings = UserReadings.objects.filter(user_id=user_id).values('ph', 'temp', 'moisture', 'humidity', 'datetime')
    ph_readings = []
    temp_readings = []
    moisture_readings = []
    humidity_readings = []
    datetimes = []
    for reading in readings:
        ph_readings.append(reading.get('ph'))
        temp_readings.append(reading.get('temp') * 100)
        moisture_readings.append(reading.get('moisture') * 100)
        humidity_readings.append(reading.get('humidity') * 100)
        datetimes.append(reading.get('datetime').isoformat())

    classifiers = UserReadings.objects.filter(user=request.user).values_list('classifier', flat=True)
    counter = Counter(classifiers)
    try:
        counter.pop(None)
    except KeyError:
        pass
    classifiers = list(counter.keys())
    context = {
        'ph_readings': ph_readings,
        'temp_readings': temp_readings,
        'moisture_readings': moisture_readings,
        'humidity_readings': humidity_readings,
        'datetimes': datetimes,
        'user': User.objects.get(id=user_id),
        'ph_mean': round(sum(ph_readings) / float(len(ph_readings)), 2) if ph_readings != [] else 0.0,
        'temp_mean': round(sum(temp_readings) / float(len(temp_readings)), 2) if temp_readings != [] else 0.0,
        'moisture_mean': round(sum(moisture_readings) / float(len(moisture_readings)), 2) if moisture_readings != [] else 0.0,
        'humidity_mean': round(sum(humidity_readings) / float(len(humidity_readings)), 2) if humidity_readings != [] else 0.0,
        'classifiers': classifiers
    }
    return render(request, 'profile.html', context)


def api_add_readings(request):
    try:
        reading = UserReadings.objects.create(user_id=request.GET.get('user_id'),
                                              ph=float(request.GET.get('ph')),
                                              humidity=float(request.GET.get('humidity')) / 100,
                                              moisture=float(request.GET.get('moisture')) / 100,
                                              temp=float(request.GET.get('temp')) / 100,
                                              datetime=timezone.now())
        new_data = [float(request.GET.get('ph')), float(request.GET.get('moisture')) / 100,
                    float(request.GET.get('humidity')) / 100, float(request.GET.get('temp')) / 100]

        reading.classifier = test_model(new_data)[0].upper()
        reading.save()

        return JsonResponse({'success': True, 'classifier': reading.classifier}, safe=False)

    except Exception as error:
        return JsonResponse({'success': False, 'classifier': None}, safe=False)
