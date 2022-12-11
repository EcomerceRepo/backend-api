from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from users_api.permissions import IsEmployee
from rest_framework.permissions import AllowAny
from django.http import Http404
from .models import Coupon
from .serializers import CouponSerializer


class CouponsList(APIView):  
    permission_classes = [AllowAny]
    def get(self, request, format=None):
        coupons = Coupon.objects.all()
        serializer = CouponSerializer(coupons, many=True)
        return Response(serializer.data)

class CouponsListEmployee(APIView):
    permission_classes = [IsEmployee]
    def post(self, request, format=None):
        serializer = CouponSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def get_object(pk):
    try:
        return Coupon.objects.get(pk=pk)
    except Coupon.DoesNotExist:
        raise Http404

class CouponDetail(APIView):
    permission_classes = [AllowAny]
    def get(self, request, pk, format=None):
        coupon = get_object(pk)
        serializer = CouponSerializer(coupon)
        return Response(serializer.data)

class CouponDetailEmployee(APIView):
    permission_classes = [IsEmployee]

  
    def put(self, request, pk, format=None):
        coupon = get_object(pk)
        serializer = CouponSerializer(coupon, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
    def patch(self, request, pk, format=None):
        coupon = get_object(pk)
        serializer = CouponSerializer(coupon,
                                           data=request.data,
                                           partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
          
  
    def delete(self, request, pk, format=None):
        coupon = self.get_object(pk)
        coupon.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)