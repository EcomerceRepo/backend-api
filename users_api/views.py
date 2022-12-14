from rest_framework.views import APIView
from . import serializers
from rest_framework.response import Response
from .models import  User
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth import authenticate, logout, login
from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions
from rest_framework.authtoken.models import Token
import jwt, datetime
from carts_api.models import Cart


class RegisterClientView(APIView):
    def post(self, request):
        userSerializer = serializers.UserSerializer(data=request.data)
        userSerializer.is_valid(raise_exception=True)
        userSerializer.save()

        return Response(userSerializer.data)

class RegisterEmployeeView(APIView):
    def post(self, request):
        userSerializer = serializers.UserSerializer(data=request.data)
        userSerializer.is_valid(raise_exception=True)
        userSerializer.save()
        return Response(userSerializer.data)
        
class LoginView(APIView):
    permission_classes = [permissions.AllowAny,]
    def post(self, request):
        email = request.data["email"]
        password = request.data["password"]
        user = User.objects.filter(email=email).first()
        if user is None:
            raise AuthenticationFailed("User not found!")
        if not user.check_password(password):
            raise AuthenticationFailed("Incorrect password!")
        login(request, user)
        payload = {
            "id": user.id,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            "iat": datetime.datetime.utcnow(),
        }
        token = jwt.encode(payload, 'secret', algorithm='HS256')
        response = Response()
        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {'Status': token}
        ## if logged user doesn't have a cart, create one
        cart = Cart.objects.filter(owner=user).first()
        if cart is None:
            Cart.objects.create(owner=user)

        return response

class UserView(APIView):
    def get(self, request):
        token = request.COOKIES.get("jwt")
        if not token:
            raise AuthenticationFailed("User unauthenticated")
        try:
            payload = jwt.decode(token, "secret", algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            raise  AuthenticationFailed("Unknown error")

        user = User.objects.filter(id=payload["id"]).first()
        serializer = serializers.UserSerializer(user)
        return Response(serializer.data)

class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie("jwt")
        response.data = {
            "Status": "Logged out!"
        }
        return response