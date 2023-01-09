from django.db import models
import users_api.models as usersApiModels
import shop_api.models as shopApiModels

class Order(models.Model):
    date_created = models.DateField(auto_now_add=True)
    date_completed = models.DateField()


    def __str__(self):
        return f"Order nr. {self.id}"

class CartItem(models.Model):
    product = models.ForeignKey(shopApiModels.Product, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(default=0)
    date = models.DateField(null=True, blank=True)

class Cart(models.Model):
    date_created = models.DateField(auto_now_add=True)
    cart_items = models.ManyToManyField(CartItem)
    owner = models.ForeignKey(usersApiModels.User, on_delete=models.CASCADE)
    description = models.CharField(default="", max_length=100)
    def __str__(self):
        return f"{self.owner.email} cart"