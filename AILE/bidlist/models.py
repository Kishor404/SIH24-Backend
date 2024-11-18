from django.db import models

class Product(models.Model):
    name=models.CharField(max_length=200,blank=False)
    seller=models.CharField(max_length=200,blank=False)
    type=models.CharField(max_length=200,blank=False)
    condition=models.IntegerField(default=0)    
    topbid=models.IntegerField(blank=False)


