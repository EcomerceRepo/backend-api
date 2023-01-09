from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime 

class User(AbstractUser):
    ROLE_CHOICES = (
        (1, 'EMPLOYEE'),
        (2, 'CLIENT')
    )
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, default=1)
    email = models.EmailField(default="", unique=True)

    def __str__(self):
        return self.email

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.IntegerField(default=0)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100, default="")
    phone_number = models.CharField(max_length=100)
    join_date = models.DateField(auto_now_add=True, null=True)