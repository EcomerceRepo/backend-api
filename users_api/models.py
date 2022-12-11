from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = (
        (1, 'EMPLOYEE'),
        (2, 'CLIENT')
    )
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, default=1)
    username = None
    email = models.EmailField(default="", unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    def __str__(self):
        return self.email
