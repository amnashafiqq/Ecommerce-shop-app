from django.shortcuts import render
from .models import Item

# Create your views here.
def items_list(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request,"./order/home.html",context)
def product_detail(request):
    return render(request,"./order/product-page.html")
    