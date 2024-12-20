from django.db import models

# Create your models here.

class Employee(models.Model):
    
    first_name = models.CharField(max_length=99)
    last_name = models.CharField(max_length=99)
    dob = models.DateField()