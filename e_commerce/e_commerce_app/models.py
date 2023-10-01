from django.db import models

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