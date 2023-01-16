from rest_framework import serializers
from carts_api.models import Cart, CartItem, Order, Favorites
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

class OrderSerializer(serializers.ModelSerializer):
    order_items = CartItemSerializer(read_only = True, many=True)
    customer = UserSerializer()
    class Meta:
        model = Order
        fields = "__all__"

class FavoritesSerializer(serializers.ModelSerializer):
    favorite_items = ProductSerializer(read_only = True, many = True)
    class Meta:
        model = Favorites
        fields = "__all__"