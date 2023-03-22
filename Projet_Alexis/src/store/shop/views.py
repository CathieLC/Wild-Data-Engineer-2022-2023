from django.shortcuts import render, redirect
from shop.models import Product, Cart, Order
from django.shortcuts import get_object_or_404
from django.urls import reverse

# Create your views here.

def index(request):
    products = Product.objects.all()
    return render(request, "shop/index.html", {"products": products})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, "shop/detail.html", {"product": product})

def add_to_cart(request, slug):
    user = request.user
    product = get_object_or_404(Product, slug=slug)
    cart, _ = Cart.objects.get_or_create(user=user)
    order, created = Order.objects.get_or_create(user=user, ordered=False, product=product)
    if created :
        cart.orders.add(order)
        cart.save()
    else:
        order.quantity += 1
        order.save()
    return redirect(reverse("product", kwargs={"slug":slug}))

def cart(request):
    cart = get_object_or_404(Cart, user=request.user)
    return render(request, "shop/cart.html", {"orders": cart.orders.all()})

def delete_cart(request):
    if cart := request.user.cart:
        cart.delete()
    return redirect("index")
