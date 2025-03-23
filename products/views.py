from django.shortcuts import render, get_object_or_404
from .models import Product
from shops.models import Shop

from django.shortcuts import render, get_object_or_404
from .models import Product, Shop

def product_list(request, shop_id):
    shop = get_object_or_404(Shop, id=shop_id)
    products = Product.objects.filter(outlet=shop)  # Use `outlet` instead of `shop` if that's the field name
    return render(request, 'product/product_list.html', {'products': products, 'shop': shop})


from django.shortcuts import render, get_object_or_404
from .models import Product

def product_details(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product/product_details.html', {'product': product})


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ProductForm
from .models import Shop

@login_required
def add_product(request):
    shop = get_object_or_404(Shop, shop_owner=request.user)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.outlet = shop  # Set the outlet (shop) for the product
            product.save()
            form.save_m2m()  # Save many-to-many fields (e.g., species)
            return redirect('shop_dashboard')
    else:
        form = ProductForm()
    
    # Debug: Print the form fields to the console
    print("Form fields:", form.fields.keys())
    
    return render(request, 'product/product_form.html', {'form': form})

@login_required
def update_product(request, product_id):
    product = get_object_or_404(Product, id=product_id, outlet__shop_owner=request.user)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('shop_dashboard')
    else:
        form = ProductForm(instance=product)
    return render(request, 'product/product_form.html', {'form': form})


@login_required
def delete_product(request, product_id):
    # Get the product and ensure it belongs to the logged-in shop owner's outlet
    product = get_object_or_404(Product, id=product_id, outlet__shop_owner=request.user)
    product.delete()
    return redirect('shop_dashboard')