from rest_framework import serializers
from carts_api.models import Cart, CartItem
from shop_api.serializers import ProductSerializer
from users_api.serializers import UserSerializer

class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    class Meta:
        model = CartItem
        fields = "__all__"

class CartSerializer(serializers.ModelSerializer):
    cart_items = CartItemSerializer(read_only = True, many=True)
    owner = UserSerializer()
    class Meta:
        model = Cart
        fields = "__all__"
    