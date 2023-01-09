from django.db import models
import users_api.models as UsersApiModels
import shop_api.models as ShopApiModels


class CartItem(models.Model):
    product = models.ForeignKey(ShopApiModels.Product, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(default=0)
    date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.product.name} x {self.quantity}'

class Order(models.Model):
    date_created = models.DateField(auto_now_add=True)
    date_completed = models.DateField()
    customer = models.ForeignKey(UsersApiModels.User, on_delete=models.CASCADE)
    order_items = models.ManyToManyField(CartItem)
    PAYMENT_METHOD_CHOICES = (
        (1, 'Paypal'),
        (2, 'Przelewy24')
    )
    payment_method = models.PositiveSmallIntegerField(choices=PAYMENT_METHOD_CHOICES, default=1)

    def __str__(self):
        return f"Order nr. {self.id}"


class Cart(models.Model):
    date_created = models.DateField(auto_now_add=True)
    cart_items = models.ManyToManyField(CartItem)
    owner = models.ForeignKey(UsersApiModels.User, on_delete=models.CASCADE)
    description = models.CharField(default="", max_length=100)
    
    def __str__(self):
        return f"{self.owner.email} cart"

    def calculate_total(self):
        total = 0
        for cart_item in self.cart_items:
            total += cart_item.quantity * cart_item.product.value
        return total