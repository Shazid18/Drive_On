from PIL import Image
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class CusProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pic')
    phone_num = models.CharField(default='+8800000000', max_length=11)
    credit_card_num = models.CharField(default='159753456', max_length=10)
    address = models.CharField(default='Address', max_length=100)
    city = models.CharField(default='City', max_length=20)
    zip_code = models.CharField(default='0000', max_length=4)

    def __str__(self):
        return f'{self.user.username} profile'

    def save(self,*args,**kwargs):
        super(CusProfile,self).save(*args,**kwargs)

        img = Image.open(self.image.path)

        if img.height > 200 or img.width > 200:
            output_size = (200, 200)
            img.thumbnail(output_size)
            img.save(self.image.path)
