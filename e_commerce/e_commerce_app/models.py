from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    product_description = models.CharField(max_length=500)
    product_publish_date = models.DateField()

