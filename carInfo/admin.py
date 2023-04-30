from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Selling_Car)
class SellCarDetailsAdmin(admin.ModelAdmin):
    list_display = ['id','model','type','price','shop_name']

@admin.register(Rental_Car)
class RentCarDetailsAdmin(admin.ModelAdmin):
    list_display = ['id','car_model','car_type','renter_name']

@admin.register(Driver)
class DriverDetailsAdmin(admin.ModelAdmin):
    list_display = ['id','dri_name','dri_lic_num']
