from django.urls import path
from . import views

urlpatterns = [
    path('<int:shop_id>/', views.product_list, name='product_list'),
]