from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class UserProfile(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    contact = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)



class UserReadings(models.Model):
    ph = models.FloatField()
    temp = models.FloatField()
    humidity = models.FloatField()
    moisture = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
