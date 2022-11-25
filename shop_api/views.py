from rest_framework.response import Response
from rest_framework.decorators import api_view
from . import models
from . import serializers

@api_view(['GET'])
def getProducts(request):
    products = models.Product.objects.all()
    productsSerializer = serializers.ProductSerializer(products, many=True)
    return Response(productsSerializer.data)

@api_view(['POST'])
def addProduct(request):
    productsSerializer = serializers.ProductSerializer(data=request.data)
    if productsSerializer.is_valid():
        productsSerializer.save()
    return Response(productsSerializer.data)

@api_view(['DELETE'])
def removeCategory(request):
    models.Product.objects.filter(id=request.data["id"]).delete()
    return Response({"reponse": "Deleted category successfully"})

@api_view(['GET'])
def getCategory(request):
    categories = models.Product.objects.all()
    categoriesSerializer = serializers.CategorySerializer(categories, many=True)
    return Response(categoriesSerializer.data)

@api_view(['POST'])
def addCategory(request):
    categorySerializer = serializers.CategorySerializer(data=request.data)
    if categorySerializer.is_valid():
        categorySerializer.save()
    return Response(categorySerializer.data)

@api_view(['DELETE'])
def removeCategory(request):
    models.Category.objects.filter(id=request.data["id"]).delete()
    return Response({"reponse": "Deleted category successfully"})

@api_view(['GET'])
def getCoupon(request):
    coupons = models.Coupon.objects.all()
    productsSerializer = serializers.CouponSerializer(coupons, many=True)
    return Response(productsSerializer.data)

@api_view(['POST'])
def addCoupon(request):
    couponsSerializer = serializers.CouponSerializer(data=request.data)
    if couponsSerializer.is_valid():
        couponsSerializer.save()
    return Response(couponsSerializer.data)

@api_view(['DELETE'])
def removeCoupon(request):
    models.Category.objects.filter(id=request.data["id"]).delete()
    return Response({"reponse": "Deleted coupon successfully"})