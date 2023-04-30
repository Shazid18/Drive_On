from django.contrib.auth.models import User
from django.db import models

from carInfo.models import Rental_Car, Selling_Car, Driver


# Create your models here.


class Sell_Car_Payment(models.Model):
    sell_car_id = models.ForeignKey(Selling_Car, on_delete=models.DO_NOTHING)
    user_profile = models.ForeignKey(User, on_delete=models.CASCADE)
    transition_id = models.CharField(max_length=15)

class Driver_Payment(models.Model):
    driver_id = models.ForeignKey(Driver, on_delete=models.DO_NOTHING)
    user_profile = models.ForeignKey(User, on_delete=models.CASCADE)
    transition_id = models.CharField(max_length=15)

class Rental_Car_payment(models.Model):
    rental_car_id = models.CharField(max_length=5)
    user_profile_id = models.CharField(max_length=5)
    transition_id = models.CharField(max_length=15)
