from django.urls import path
from .views import RegisterView,LoginView,UserView,LogoutView,HomeView
urlpatterns = [
     path('register/',RegisterView.as_view()),
     path('login/',LoginView.as_view(),name='login'),
     path('logout/',LogoutView.as_view()),
     path('user/',UserView.as_view()),
     path('', HomeView.as_view(), name='home_page'),




]
