from django.db import models
import users_api.models as usersApiModels
import shop_api.models as shopApiModels

class Order(models.Model):
    dateCreated = models.DateField(auto_now_add=True)
    dateCompleted = models.DateField()
    isCompleted = models.BooleanField()
    isAbandoned = models.BooleanField()

    def __str__(self):
        return f"Order nr. {self.id}"

class Cart(models.Model):
    dateCreated = models.DateField(auto_now_add=True)
    products = models.ManyToManyField(shopApiModels.Product)
    def __str__(self):
        return f"Cart nr. {self.id}"