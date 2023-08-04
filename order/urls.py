from django.urls import path
from .views import checkout,add_to_cart,remove_from_cart
from . import views

app_name = "order"

urlpatterns=[
    # path('home/',home,name='itemslist'),
    # path('product/',product_detail ,name='productdetail'),
    path('product/<slug>/',views.ItemDetailView.as_view() ,name='productdetail'),
    path('checkout/',checkout,name='checkout'),
    path('home/', views.HomeView.as_view(), name='itemslist'),
    path('add_to_cart/<slug>/',add_to_cart,name ='add-to-cart'),
    path('remove_from_cart/<slug>/',remove_from_cart,name='remove-from-cart'),



]