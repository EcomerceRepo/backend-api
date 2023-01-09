from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('get_cart/', views.CartView.as_view()),
    path('update_cart/', views.CartProductView.as_view()), 
]
