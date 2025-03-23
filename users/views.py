from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

from cart.models import Cart
from .models import Customer

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Check if a Customer profile already exists for the user
            if not hasattr(user, 'customer'):
                Customer.objects.create(user=user)  # Create a Customer profile only if it doesn't exist
            login(request, user)
            return redirect('customer_dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

# User Login
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('customer_dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

def customer_logout(request):
    logout(request)
    return redirect('index_dashboard')



from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from shops.models import Shop
from products.models import Product

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CustomerProfileForm
from .models import Customer

@login_required
def customer_dashboard(request):
    # Get the selected location from the request (if any)
    selected_location = request.GET.get('location')

    # Fetch all shops (or filter based on location)
    if selected_location:
        shops = Shop.objects.filter(location=selected_location)
    else:
        shops = Shop.objects.all()

    # Fetch all unique locations for the filter dropdown
    locations = Shop.objects.values_list('location', flat=True).distinct()

    # Handle profile update form submission
    if request.method == 'POST':
        profile_form = CustomerProfileForm(request.POST, request.FILES, instance=request.user.customer)
        if profile_form.is_valid():
            profile_form.save()
    else:
        profile_form = CustomerProfileForm(instance=request.user.customer)

    return render(request, 'users/dashboard.html', {
        'shops': shops,
        'locations': locations,
        'selected_location': selected_location,
        'profile_form': profile_form,  # Pass the profile form to the template
    })

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from shops.models import Shop
from products.models import Product

@login_required
def shop_products(request, shop_id):
    shop = get_object_or_404(Shop, id=shop_id)
    products = Product.objects.filter(outlet=shop)
    
    # Get or create the cart for the current user and shop
    cart, created = Cart.objects.get_or_create(customer=request.user.customer, outlet=shop)
    
    # Calculate the percentage of calories filled
    total_calories = cart.total_calories
    calorie_limit = cart.calorie_limit
    total_calories_percentage = (total_calories / calorie_limit) * 100 if calorie_limit > 0 else 0
    
    return render(request, 'users/shop_products.html', {
        'shop': shop,
        'products': products,
        'cart': cart,
        'total_calories_percentage': total_calories_percentage,
    })

