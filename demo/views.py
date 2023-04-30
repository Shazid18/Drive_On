from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.urls import reverse_lazy

from carInfo.models import Rental_Car, Selling_Car, Driver
from cusProfile.models import CusProfile
from payment.models import *
from rentInfo.models import Rent_Car_Record
from .form import CreateUserFrom, PasswordChangingForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required

# Create your views here.

#idex page load korbe
def index(request):
    return render(request, 'index.html')


#Login kora thakle home page load korbe
# if we need to restict any page with login then we need to write the 12 num line code before that pages method line
@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')