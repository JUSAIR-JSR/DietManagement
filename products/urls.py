from django.urls import path
from . import views

urlpatterns = [
    path('shops/<int:shop_id>/products/', views.product_list, name='product_list'),
    path('product/add/', views.add_product, name='add_product'),
    path('product/update/<int:product_id>/', views.update_product, name='update_product'),
    path('product/delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('products/<int:product_id>/', views.product_details, name='product_details'),

]