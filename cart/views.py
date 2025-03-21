from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from products.models import Product
from .models import Cart, CartItem
from orders.models import Order, OrderItem

@login_required
def view_cart(request):
    # Fetch all carts for the current customer
    carts = Cart.objects.filter(customer=request.user.customer).select_related('outlet')
    return render(request, 'cart/cart.html', {'carts': carts})

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    outlet = product.outlet  # Get the outlet associated with the product

    # Get or create a cart for the customer and the specific outlet
    cart, created = Cart.objects.get_or_create(customer=request.user.customer, outlet=outlet)

    # Check if adding the product exceeds the calorie limit
    total_calories = cart.total_calories + (product.calories_per_100g * 1)  # Default quantity is 1
    if total_calories > cart.calorie_limit:
        messages.error(request, "Adding this product will exceed your calorie limit.")
        return redirect('view_cart')

    # Add the product to the cart
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    messages.success(request, "Product added to cart successfully.")
    return redirect('view_cart')

@login_required
def update_quantity(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id, cart__customer=request.user.customer)
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'increase':
            cart_item.quantity += 1
        elif action == 'decrease' and cart_item.quantity > 1:
            cart_item.quantity -= 1
        cart_item.save()
    return redirect('view_cart')

@login_required
def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id, cart__customer=request.user.customer)
    cart_item.delete()
    return redirect('view_cart')

@login_required
def place_order(request, cart_id):
    cart = get_object_or_404(Cart, id=cart_id, customer=request.user.customer)
    if cart.items.count() == 0:
        return redirect('view_cart')  # No items in cart

    # Create the order
    order = Order.objects.create(
        customer=request.user.customer,
        outlet=cart.outlet,  # Use the outlet associated with the cart
        total_calories=cart.total_calories  # Save the total calories of the order
    )

    # Add cart items to the order
    for cart_item in cart.items.all():
        OrderItem.objects.create(
            order=order,
            product=cart_item.product,
            quantity=cart_item.quantity
        )

    # Clear the cart
    cart.items.all().delete()

    messages.success(request, "Order placed successfully.")
    return redirect('order_success')  # Redirect to the order success page