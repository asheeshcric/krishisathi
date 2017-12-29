from django.contrib import admin

# Register your models here.
from .models import User_Data, User_Info

admin.site.register(User_Info)
admin.site.register(User_Data)
