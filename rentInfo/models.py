from django.contrib.auth.models import User
from django.db import models

from carInfo.models import Rental_Car


# Create your models here.

class Rent_Car_Record(models.Model):
    rent_car_id = models.ForeignKey(Rental_Car, on_delete=models.DO_NOTHING)
    user_profile = models.ForeignKey(User, on_delete=models.CASCADE)
    rent_time = models.DateTimeField()
    return_time = models.DateTimeField()
    pickup_loc = models.CharField(max_length=100)
