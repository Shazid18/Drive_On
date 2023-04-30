from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profile(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    user_name = models.CharField(max_length=20)
    email_add = models.EmailField()
    phone_num = models.CharField(max_length=11)
    birth_date = models.DateField()
    credit_card_num = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=20)
    zip_code = models.IntegerField()
    profile_pic = models.ImageField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
