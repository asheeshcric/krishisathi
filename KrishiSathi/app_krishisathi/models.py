from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class User_Info(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    COUNTRY_CHOICES = (
        ('NPL', 'Nepal'),
        ('IND', 'India'),
        ('BAN', 'Bangladesh'),
        ('PAK', 'Pakistan'),
        ('BHU', 'Bhutan'),
        ('AFG', 'Afghanistan'),
    )
    country = models.CharField(max_length=20, choices=COUNTRY_CHOICES)
    devicecode = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

class User_Data(models.Model):
    moisture = models.FloatField(default=50.0)
    pH = models.FloatField(default=7.0)
    humidity = models.FloatField(default=50.0)
    temperature = models.FloatField(default=25.0)
    datetime = models.CharField(max_length=30)
    devicecode = models.IntegerField(default=0)
