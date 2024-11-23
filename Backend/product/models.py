from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200, blank=False)
    details = models.CharField(max_length=200, blank=False)
    quality = models.IntegerField(blank=False,default=10)
    seller_id = models.CharField(max_length=200, blank=False)
    quantity = models.CharField(max_length=200, blank=False)
    device_id= models.CharField(max_length=200, blank=False)
