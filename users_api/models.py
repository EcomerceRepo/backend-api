from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = (
        (1, 'EMPLOYEE'),
        (2, 'CLIENT')
    )
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, default=1)

    def __str__(self):
        return self.email

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    balance = models.IntegerField(default=0)
    joinDate = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=200, default="")
    phoneNumber = models.CharField(max_length=15, default="")
    def __str__(self):
        return self.user.email if self.user != None else self.pk

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    department = models.CharField(max_length=30, default="")
    joinDate = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user.email if self.user != None else self.pk