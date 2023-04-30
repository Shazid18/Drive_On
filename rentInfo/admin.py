from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Rent_Car_Record)
class RentCarRecordDetailsAdmin(admin.ModelAdmin):
    list_display = ['id','rent_car_id','user_profile','rent_time','return_time']