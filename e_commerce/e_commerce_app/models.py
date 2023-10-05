from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    product_description = models.CharField(max_length=500)
    product_publish_date = models.DateField()
    product_category = models.CharField(max_length=70)
    product_sub_category = models.CharField(max_length=70)
    product_price = models.IntegerField()
    product_image = models.ImageField(upload_to="e_commerce_app/images")


    def __str__(self):
        return self.product_name


# class UserProfile(models.Model):
#     """For storing customize user details"""
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#
#
# class OTP(models.Model):
#     """For storing OTP details"""
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     otp_code = models.CharField(max_length=6)
#     is_verified = models.BooleanField(default=False)
