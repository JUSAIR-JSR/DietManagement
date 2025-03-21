from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.shop_login, name='shop_login'),
    path('logout/', views.shop_logout, name='shop_logout'),
    path('dashboard/', views.shop_dashboard, name='shop_dashboard'),
    path('profile/', views.shop_profile, name='shop_profile'),
    path('product/add/', views.add_product, name='add_product'),
    path('product/update/<int:product_id>/', views.update_product, name='update_product'),
    path('product/delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('orders/', views.shop_orders, name='shop_orders'),
]