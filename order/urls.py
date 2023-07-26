from django.urls import path
from .views import items_list,product_detail

urlpatterns=[
    path('items_list/',items_list,name='itemslist'),
    path('product/',product_detail,name='productdetail')

]