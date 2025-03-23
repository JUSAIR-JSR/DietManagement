from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from orders.models import Order
from .models import Shop
from products.models import Product
from .forms import ProductForm  # Import the ProductForm

@login_required
def shop_dashboard(request):
    # Get the shop (outlet) owned by the logged-in user
    shop = get_object_or_404(Shop, shop_owner=request.user)
    
    # Filter products by the outlet (shop)
    products = Product.objects.filter(outlet=shop)
    
    return render(request, 'shops/dashboard.html', {'shop': shop, 'products': products})

@login_required
def shop_profile(request):
    shop = get_object_or_404(Shop, shop_owner=request.user)
    return render(request, 'shops/shop_profile.html', {'shop': shop})




@login_required
def shop_orders(request):
    shop = get_object_or_404(Shop, shop_owner=request.user)
    orders = Order.objects.filter(outlet=shop)  # Use `outlet` instead of `shop`
    return render(request, 'shops/order_list.html', {'orders': orders})

# Shop Owner Login
def shop_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and hasattr(user, 'shop'):  # Check if the user is a shop owner
                login(request, user)
                return redirect('shop_dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'shops/shop_login.html', {'form': form})

def shop_logout(request):
    logout(request)
    return redirect('index_dashboard')