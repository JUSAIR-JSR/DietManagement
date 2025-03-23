from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.shop_login, name='shop_login'),
    path('logout/', views.shop_logout, name='shop_logout'),
    path('dashboard/', views.shop_dashboard, name='shop_dashboard'),
    path('profile/', views.shop_profile, name='shop_profile'),
    path('orders/', views.shop_orders, name='shop_orders'),
]