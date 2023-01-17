from rest_framework import serializers
from . import models

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'

class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Coupon
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=models.Category.objects.all())
    coupon = serializers.PrimaryKeyRelatedField(queryset=models.Coupon.objects.all(), required=False)
    class Meta:
        model = models.Product
        fields = ['name', 'value', 'description', 'address', 'category', 'coupon']
