from django.db import models

class Device(models.Model):
    product_id = models.CharField(max_length=200, blank=False, default="0")
    reading_temperature = models.CharField(max_length=200)
    reading_humidity = models.CharField(max_length=200)
    maintain_temperature = models.CharField(max_length=200)
    maintain_humidity = models.CharField(max_length=200)
    
