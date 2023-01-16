from rest_framework.views import APIView
from users_api.permissions import IsClient
from rest_framework.response import Response
from users_api.utils import getUserByToken
from .models import Cart, CartItem, Order, Favorites
from .serializers import CartSerializer, OrderSerializer, FavoritesSerializer
from users_api.serializers import UserSerializer
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
            return Response({"Status": f"Your cart is empty! Add some products to place the order"})

    def get(self, request):
        user = getUserByToken(request)
        option = request.data["option"]
        if option == "historical":
            orders = Order.objects.filter(customer=user, isCompleted=True)
        elif option == "pending":
            orders = Order.objects.filter(customer=user, isCompleted=False)
        elif option == "all":
            orders = Order.objects.filter(customer=user)
        serializer = OrderSerializer(orders, many=True)
        return Response({"data": serializer.data})

    def delete(self, request):
        order_id = request.data["id"]
        user = getUserByToken(request)
        order = Order.objects.filter(id=order_id).first()
        if order is None:
            return Response({"Status": "This order doesn't exist!"})
        order_total_cost = order.calculate_total()
        order.delete()
        user.client.balance += order_total_cost
        user.save()
        return Response({"Status": "Order has been cancelled, funds have been restored to your account!"})

class BalanceView(APIView):
    permission_classes=[IsClient]

    def get(self, request):
        user = getUserByToken(request)
        return Response({"Balance of currently logged user": user.client.balance })

    def post(self, request):
        balance = request.data["balance"]
        user = getUserByToken(request)
        user.client.balance += balance
        user.client.save()
        serializer = UserSerializer(user)
        return Response(serializer.data)

class FavoritesView(APIView):
    def get(self, request):
        user = getUserByToken(request)
        favorites = Favorites.objects.get(owner=user)
        serializer = FavoritesSerializer(favorites)
        return Response(serializer.data)
    
    def post(self, request):
        user = getUserByToken(request)
        favorites = Favorites.objects.get(owner=user)
        product_id = request.data["id"]
        product = get_product(product_id)
        favorite_item = favorites.favorite_items.filter(favorite_item=product).first()
        if favorite_item is not None:
            return Response({"Status": f"Product {product.name} is already in your favorites"}) 
        else:
            favorites.favorite_items.add(favorite_item)
        return Response({"Status": f"Product {product.name} was added to your favorites"})

    def delete(self, request):
        user = getUserByToken(request)
        favorites = Favorites.objects.get(owner=user)
        product_id = request.data["id"]
        product = get_product(product_id)
        favorite_item = favorites.favorite_items.filter(product=product).first()
        if favorite_item is not None:
            favorites.cart_items.remove(favorite_item)
            return Response({"Status": f"Product {product.name} was removed from favorites"})
        else:
            return Response({"Status": f"This item is not in your favorites"})