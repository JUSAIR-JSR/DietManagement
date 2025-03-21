from django.urls import path
from . import views

urlpatterns = [
    # path('place/', views.place_order, name='place_order'),
    path('history/', views.order_history, name='order_history'),
    path('update/<int:order_id>/', views.update_order_status, name='update_order_status'),
    path('success/', views.order_success, name='order_success'),
    path('status/<int:order_id>/', views.order_status, name='order_status'),


]