from rest_framework import serializers
from .models import User_Data, User_Info
#from django.contrib.auth.models import User


class User_DataSerializer(serializers.ModelSerializer):

    class Meta:
        model = User_Data
        fields = "__all__"

class User_InfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = User_Info
        fields = ('user', 'gender', 'country', 'devicecode')
        #fields = "__all__"