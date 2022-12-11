from django.urls import path
from . import product_views
from . import category_views
from . import coupon_views

urlpatterns = [
    path('product', product_views.ProductsList.as_view()),
    path('product/<int:pk>/', product_views.ProductDetails.as_view()),
    path('category/', category_views.CategoriesList.as_view()),
    path('category/<int:pk>/', category_views.CategoryDetail.as_view()),
    path('product/', coupon_views.CouponsList.as_view()),
    path('product/<int:pk>/', coupon_views.CouponDetail.as_view()),
]