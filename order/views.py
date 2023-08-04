from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from .models import Item, Order,OrderItem
from django.utils import timezone
from django.contrib import messages

# # Create your views here.
# def home(request):
#     context = {
#         'items': Item.objects.all()
#     }
#     return render(request,"./order/home.html",context)

# def product_detail(request):
#     return render(request,"./order/product-page.html")

def checkout(request):
    return render(request,"./order/checkout-page.html")

class HomeView(ListView):
    model = Item
    template_name = './order/home.html'
    
class ItemDetailView(DetailView):
    model = Item
    template_name = "./order/product-page.html"

def add_to_cart(request,slug):
    item = get_object_or_404(Item, slug = slug)
    order_item, created = OrderItem.objects.get_or_create(item=item,user=request.user,ordered=False)
    order_qs = Order.objects.filter(user = request.user,ordered =False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug = item.slug).exists():
            order_item.quantity +=1
            order_item.save()
            messages.info(request,f"Another {order_item.quantity} {item.title} added to cart")

        else:
            messages.info(request,"This item was added to your cart")
            order.items.add(order_item)
    else:
        order_date = timezone.now()
        order = Order.objects.create(user = request.user,ordered_date=order_date)
        order.items.add(order_item)
        messages.info(request,"This item was added to your cart")

    return redirect ( "order:productdetail", slug = slug )

def remove_from_cart(request,slug):
    item = get_object_or_404(Item, slug = slug)
    order_qs = Order.objects.filter(user = request.user,ordered =False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug = item.slug).exists():
            order_item, created = OrderItem.objects.filter(item=item,user=request.user,ordered=False)[0]
            order.items.remove(order_item)
            messages.info(request,"This item was removed from your cart")
        else:
            messages.info(request,"This item was not in your cart")
            return redirect ( "order:productdetail", slug = slug )

    else:
        messages.info(request,"You donot have an active order")

        return redirect ( "order:productdetail", slug = slug )

    return redirect ( "order:productdetail", slug = slug )



    