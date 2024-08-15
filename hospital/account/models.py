from django.db import models

# Create your models here.

class Patient(models.Model):
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    age=models.PositiveIntegerField()
    phone=models.IntegerField()
    
