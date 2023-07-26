from django.urls import path
from .views import items_list

urlpatterns=[
    path('items_list/',items_list,name='itemslist')
]