from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop_api.urls')),
    path('carts/', include('carts_api.urls')),
    path('auth/', include('users_api.urls')),
]
