from django.shortcuts import render, get_object_or_404
from .models import Product
from shops.models import Shop

def product_list(request, shop_id):
    shop = get_object_or_404(Shop, id=shop_id)
    products = Product.objects.filter(shop=shop)
    return render(request, 'products/product_list.html', {'products': products, 'shop': shop})