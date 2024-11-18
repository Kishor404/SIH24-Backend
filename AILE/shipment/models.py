from django.db import models

class Product(models.Model):
    ProductId = models.CharField(max_length=200, blank=False)
    seller = models.CharField(max_length=200, unique=True, blank=False)
    location = models.JSONField(default={"lon": 0, "lat": 0})
    status = models.CharField(max_length=200,blank=False, default="initailize")


    def __str__(self):
        return f"{self.name} ({self.seller})"
