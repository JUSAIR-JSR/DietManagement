from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.customer_logout, name='customer_logout'),
    path('dashboard/', views.customer_dashboard, name='customer_dashboard'),
    path('shop/<int:shop_id>/', views.shop_products, name='shop_products'),


]