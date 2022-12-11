from django.urls import path
from . import product_views
from . import category_views
from . import coupon_views

urlpatterns = [
    path('product/', product_views.ProductsList.as_view()),
    path('product-employee/', product_views.ProductsListEmployee.as_view()),
    path('product/<int:pk>/', product_views.ProductDetails.as_view()),
    path('product-employee/<int:pk>/', product_views.ProductDetailsEmployee.as_view()),
    path('category/', category_views.CategoriesList.as_view()),
    path('category-employee/', category_views.CategoriesListEmployee.as_view()),
    path('category/<int:pk>/', category_views.CategoryDetail.as_view()),
    path('category-employee/<int:pk>/', category_views.CategoryDetailEmployee.as_view()),
    path('coupon/', coupon_views.CouponsList.as_view()),
    path('coupon-employee/', coupon_views.CouponsListEmployee.as_view()),
    path('coupon/<int:pk>/', coupon_views.CouponDetail.as_view()),
    path('coupon-employee/<int:pk>/', coupon_views.CouponDetailEmployee.as_view()),
]