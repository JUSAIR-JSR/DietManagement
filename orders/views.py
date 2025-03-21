from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Order, OrderItem
from shops.models import Shop
from cart.models import Cart, CartItem



from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Order

@login_required
def order_history(request):
    # Fetch all orders for the current user
    orders = Order.objects.filter(customer=request.user.customer).order_by('-created_at')
    return render(request, 'orders/order_history.html', {'orders': orders})

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Order

@login_required
def update_order_status(request, order_id):
    order = get_object_or_404(Order, id=order_id, shop__shop_owner=request.user)
    if request.method == 'POST':
        new_status = request.POST.get('status')
        order.status = new_status
        order.save()
        return redirect('shop_orders')
    return render(request, 'orders/update_status.html', {'order': order})


from django.shortcuts import render

def order_success(request):
    return render(request, 'orders/order_success.html')


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Order

@login_required
def order_success(request):
    # Get the latest order for the current user
    order = Order.objects.filter(customer=request.user.customer).last()
    if not order:
        return redirect('customer_dashboard')  # No order found
    return render(request, 'orders/order_success.html', {'order': order})

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Order

@login_required
def order_status(request, order_id):
    order = get_object_or_404(Order, id=order_id, customer=request.user.customer)
    return render(request, 'orders/order_status.html', {'order': order})