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


#sign-up er kaj korsi
def registration(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserFrom()

        if request.method == 'POST': #form theke data netese
            form = CreateUserFrom(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for '+ user)
                return redirect('login')

        context = {'form': form}
        return render(request, 'registration.html', context)

#login page er kaj korsi
def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:

        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth_login(request, user)
                return redirect('home')
            else:
                messages.info(request,'Username or Password is incorrect')


        context = {}
        return render(request, 'login.html', context) #login hobe


#logout er kaj korsi
def logoutUser(request):
    logout(request)
    return redirect('index')


#password Update er kaj korsi
class PasswordsChangeView(PasswordChangeView):

    form_class = PasswordChangingForm

    success_url = reverse_lazy('view-profile')


# dorkar nai ei page.ei page er kaj holo password change korle ekta success msg dey
# def password_Success(request):
#     return render(request,'password_success.html', {})
