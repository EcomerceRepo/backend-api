from django.db import models

class Category(models.Model):
    name = models.CharField(max_length = 20)
    dateAdded = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class Coupon(models.Model):
    code = models.CharField(max_length = 10)
    discountPercent = models.IntegerField()
    dateAdded = models.DateTimeField(auto_now_add=True)
    expirationDate = models.DateField()
    def __str__(self):
        return self.code


class Product(models.Model):
    name = models.CharField(max_length = 30)
    value = models.IntegerField(default=0)
    dateAdded = models.DateTimeField(auto_now_add=True)
    discout = models.IntegerField(default=0)
    imageURL = models.ImageField(default="")
    description = models.TextField(max_length=400, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    coupon = models.ForeignKey(Coupon, on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        return self.name