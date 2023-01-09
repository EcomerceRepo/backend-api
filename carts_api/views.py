from rest_framework.views import APIView
from users_api.permissions import IsClient
from rest_framework.response import Response
from users_api.utils import getUserByToken
from .models import Cart, CartItem
from .serializers import CartSerializer
from shop_api.utils import get_product

class CartView(APIView):
    permission_classes = [IsClient]
    def get(self, request):
        user = getUserByToken(request)
        cart = Cart.objects.get(owner=user)
        serializer = CartSerializer(cart)
        return Response(serializer.data)

class CartProductView(APIView):
    permission_classes = [IsClient]
    def post(self, request):
        user = getUserByToken(request)
        cart = Cart.objects.get(owner=user)
        product_id = request.data["id"]
        quantity = request.data["quantity"]
        product = get_product(product_id)
        cart_item = cart.cart_items.filter(product=product).first()
        if cart_item is not None:
            cart_item.quantity += quantity
            cart_item.save()
        else:
            cart_item = CartItem.objects.create(quantity=quantity, product=product)
            cart.cart_items.add(cart_item)
        return Response({"Status": f"Product {product.name} was added to your cart"})

    def delete(self, request):
        user = getUserByToken(request)
        cart = Cart.objects.get(owner=user)
        product_id = request.data["id"]
        # quantity = request.data["quantity"]
        product = get_product(product_id)
        cart_item = cart.cart_items.filter(product=product).first()
        if cart_item is not None:
            cart.cart_items.remove(cart_item)
            return Response({"Status": f"Product {product.name} was removed from your cart"})
        else:
            return Response({"Status": f"This item is not in your cart"})
