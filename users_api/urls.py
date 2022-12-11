from django.urls import path
from . import views

urlpatterns = [
    path('register-client/', views.RegisterView.as_view()),
    path('login-client/', views.LoginView.as_view()),
    path('logout-client/', views.LogoutView.as_view()),
    path('user/', views.UserView.as_view()),
]