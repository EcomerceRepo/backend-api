from rest_framework.views import APIView
from users_api.permissions import IsClient
from rest_framework.response import Response
from users_api.utils import getUserByToken
from .models import Cart, CartItem, Order
from .serializers import CartSerializer, OrderSerializer
from shop_api.utils import get_product
import datetime

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

class CheckoutView(APIView):
    permission_classes=[IsClient]
    def post(self, request):
        user = getUserByToken(request)
        cart = Cart.objects.get(owner=user)
        total_cart_cost = cart.calculate_total()
        payment_method = request.data['payment_method']
        print(total_cart_cost)
        if cart.cart_items.count() > 0 and total_cart_cost < user.client.balance:
            order = Order.objects.create(customer=user, date_completed = datetime.datetime.now(), payment_method = payment_method)
            for cart_item in cart.cart_items.all():
                order.order_items.add(cart_item)
            cart.cart_items.clear()
            user.client.balance -= total_cart_cost
            user.save()
            return Response({"Status": f"Your order was placed!"})
        else:
            return Response({"Status": f"Your cart is empty!"})

    def get(self, request):
        user = getUserByToken(request)
        orders = Order.objects.filter(customer=user)
        serializer = OrderSerializer(orders, many=True)
        return Response({"data": serializer.data})

    def delete(self, request):
        pass