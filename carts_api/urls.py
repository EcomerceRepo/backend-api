from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('get_cart/', views.CartView.as_view()),
    path('update_cart/', views.CartProductView.as_view()), 
    path('checkout/', views.CheckoutView.as_view()),
    path('balances/', views.BalanceView.as_view()),
    path('favorites/', views.FavoritesView.as_view()),
]
