"""pythonProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
import demo.views as driveon

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', driveon.index, name='index'),
    path('home/', driveon.home, name='home'),
    path('registration/', driveon.registration, name='registration'),
    path('login/', driveon.login, name='login'),
    path('logout/', driveon.logoutUser, name='logout'),
    path('change-password/', driveon.PasswordsChangeView.as_view(template_name='change-password.html'), name='change-password'),
    # path('password_success/', driveon.password_Success, name='password_success'),
    path('rent-car/', driveon.rent_car, name='rent-car'),
    path('booking-details/<int:pk>/<str:id>', driveon.booking_details, name='booking-details'),
    path('rent-payment-confirmation/', driveon.rentPaymentconformation, name='rent-payment-confirmation'),
    path('buy-car/', driveon.Buy_car, name='buy-car'),


]
