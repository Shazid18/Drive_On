from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Profile)
class SellCarDetailsAdmin(admin.ModelAdmin):
    list_display = ['id','first_name','last_name']
