from django.db import models

# Create your models here.
# model class e amra data store korar jonno table(class) create kore

class Selling_Car(models.Model):
    CAR_TYPE = (
        ('Sedan', 'Sedan'),
        ('SUV', 'SUV'),
        ('Van', 'Van'),
        ('Micro', 'Micro'),
        ('Jeep', 'Jeep'),
    )

    model = models.CharField(max_length=50)
    type = models.CharField(max_length=20, choices=CAR_TYPE)
    price = models.CharField(max_length=15)
    fuel_type = models.CharField(max_length=10)
    eng_displacement = models.CharField(max_length=15)
    eng_torque = models.CharField(max_length=50)
    no_of_cylinder = models.IntegerField()
    ground_clearance = models.CharField(max_length=10)
    kerb_weight = models.CharField(max_length=10)
    boot_space = models.CharField(max_length=10)
    shop_name = models.CharField(max_length=100)
    shop_address = models.CharField(max_length=300)
    advance = models.CharField(max_length=300)
    availability = models.CharField(max_length=20)
    car_image = models.ImageField(upload_to='media')

    def __str__(self):
        return self.model


class Rental_Car(models.Model):
    CAR_TYPE = (
        ('Sedan', 'Sedan'),
        ('SUV', 'SUV'),
        ('Van', 'Van'),
        ('Micro', 'Micro'),
    )

    car_num = models.CharField(max_length=20)
    seating_capacity = models.IntegerField()
    fuel_type = models.CharField(max_length=15)
    car_type = models.CharField(max_length=20, choices=CAR_TYPE)
    car_colour = models.CharField(max_length=10)
    car_mileage = models.CharField(max_length=5) #charField dibo
    car_model = models.CharField(max_length=50)
    renter_name = models.CharField(max_length=50)
    renter_phone_num = models.CharField(max_length=11)
    rate_per_hour = models.CharField(max_length=10) #rate per hour hobe
    rate_per_day = models.CharField(max_length=10)
    car_image = models.ImageField(upload_to='media')

    def __str__(self):
        return self.car_num + ' ' + self.renter_name

class Driver(models.Model):

    dri_name = models.CharField(max_length=20)
    dri_age = models.CharField(max_length=2)#charField nibo
    dri_address = models.CharField(max_length=300)
    dri_experience = models.CharField(max_length=50)
    dri_lic_num = models.CharField(max_length=50)
    accident_history = models.TextField(max_length=100)
    expected_salary = models.CharField(max_length=15)
    dri_img = models.ImageField(upload_to='media')
    dri_phone_num = models.CharField(max_length=11)

    def __str__(self):
        return self.dri_name
