from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Sell_Car_Payment)
class SellCarPaymentDetailsAdmin(admin.ModelAdmin):
    list_display = ['id','sell_car_id','user_profile','transition_id']

@admin.register(Driver_Payment)
class DriverPaymentDetailsAdmin(admin.ModelAdmin):
    list_display = ['id','driver_id','user_profile','transition_id']

@admin.register(Rental_Car_payment)
class RentalCarPaymentDetailsAdmin(admin.ModelAdmin):
    list_display = ['id','rental_car_id','user_profile_id','transition_id']