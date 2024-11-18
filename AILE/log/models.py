from django.db import models

class User(models.Model):
    name=models.CharField(max_length=200,default="None")
    phone=models.CharField(max_length=10,unique=True,blank=False)
    password=models.CharField(max_length=20,blank=False)
    role=models.CharField(max_length=20,blank=False,default="customer")