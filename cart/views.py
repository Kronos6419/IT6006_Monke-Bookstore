from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Cart, CartItem, Order, Profile, Book
from accounts.models import Profile
from django.contrib import messages
from django.utils import timezone

# Create your views here.

@login_required
def cart_detail(request):
    profile, _ = Profile.objects.get_or_create(user=request.user)
    cart, _ = Cart.objects.get_or_create(profile=profile)
    cart_items = CartItem.objects.filter(cart=cart)
    
    return render(request, "cart/cart.html", {
        "cart_items": cart_items,
        "total_amount": cart.total_amount,
    })


@login_required
def update_cart_item(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, cart__profile__user=request.user)
    
    if request.method == "POST":
        try:
            quantity = int(request.POST.get("quantity", 0))
        except ValueError:
            quantity = 0
        if quantity <= 0:
            item.delete()
        else:
            item.quantity = quantity
            item.save()
    return redirect("cart_detail")


@login_required
def place_order(request):
    profile, _ = Profile.objects.get_or_create(user=request.user)
    cart = get_object_or_404(Cart, profile=profile)
    cart_items = CartItem.objects.filter(cart=cart)

    if not cart_items.exists():
        return redirect("cart_detail")

    order = Order.objects.create(
        customer=profile,
        total_amount=cart.total_amount,
        date=timezone.now()
    )
    cart_items.delete()

    messages.success(
        request, 
        f"Your Order Has Been Placed. | Amount Paid: ${order.total_amount} | Ordered On: {order.date.strftime('%d-%m-%Y-%m')}"
    )

    return redirect("cart_detail")