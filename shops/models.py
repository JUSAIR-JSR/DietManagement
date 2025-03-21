from django.db import models
from django.contrib.auth.models import User

class Shop(models.Model):
    shop_owner = models.OneToOneField(User, on_delete=models.CASCADE)
    shop_name = models.CharField(max_length=255)
    profile_photo = models.ImageField(upload_to='shop_profile_photos/', blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.shop_name   