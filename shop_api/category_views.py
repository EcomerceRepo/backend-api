from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from django.http import Http404
from .models import Category
from .serializers import CategorySerializer
from users_api.permissions import IsEmployee
from rest_framework.permissions import AllowAny


class CategoriesList(APIView):  
    permission_classes = [AllowAny]
    def get(self, request, format=None):
        categorys = Category.objects.all()
        serializer = CategorySerializer(categorys, many=True)
        return Response(serializer.data)
class CategoriesListEmployee(APIView):  
    permission_classes = [IsEmployee]
    def post(self, request, format=None):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def get_object(pk):
    try:
        return Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        raise Http404

class CategoryDetail(APIView):
    permission_classes = [AllowAny]
  
    def get(self, request, pk, format=None):
        category = get_object(pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

class CategoryDetailEmployee(APIView):
    permission_classes = [IsEmployee]
    def put(self, request, pk, format=None):
        category = get_object(pk)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
    def patch(self, request, pk, format=None):
        category = self.get_object(pk)
        serializer = CategorySerializer(category,
                                           data=request.data,
                                           partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
          
  
    def delete(self, request, pk, format=None):
        category = self.get_object(pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

