from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import AllowAny
from  users_api.permissions import IsClient, IsEmployee
from .models import Product
from .serializers import ProductSerializer
from .utils import get_product

class ProductsList(APIView):
    permission_classes = [AllowAny]
    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class ProductsListEmployee(APIView):
    permission_classes=[IsEmployee]
    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductDetails(APIView):
    permission_classes = [AllowAny]
    def get(self, request, pk, format=None):
        product = get_product(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
        
class ProductDetailsEmployee(APIView):
    permission_classes = [IsEmployee]
    def put(self, request, pk, format=None):
        product = get_product(pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
    def patch(self, request, pk, format=None):
        product = get_product(pk)
        serializer = ProductSerializer(product,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
          
  
    def delete(self, request, pk, format=None):
        product = get_product(pk)
        product.delete()
        return Response({"Response": "Product deleted successfully"})



