from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer
from rest_framework.exceptions import AuthenticationFailed
import jwt,datetime
from django.views import View
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

# Create your views here.

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data= request.data)
      
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = redirect('login')
        return response
    def get(self, request):
        return render(request, "authentication/Signup.html")
     
    

class LoginView(View):
    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)

            # Create JWT token
            payload = {
                'id': user.id,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
                'iat': datetime.datetime.utcnow()
            }

            token = jwt.encode(payload, 'your_secret_key', algorithm='HS256')

            # Create a response with a cookie and redirect to home_page
            response = redirect('home_page')
            response.set_cookie(key='jwt', value=token, httponly=True)
            return response
        else:
            return HttpResponse('Invalid credentials. Please try again.')


    def get(self, request):
        return render(request, "authentication/Login.html")
     
class UserView(APIView):
    def get(self,request):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed("Unauthenticated")
        try:
            payload = jwt.decode(token,'secret',algorithms=['HS256'])
        except jwt.ExpiredSignatureError:          
            raise AuthenticationFailed('Unauthenticated')
        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)
        return Response(serializer.data)
class LogoutView(APIView):
    def post(self,request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message':'success'
        }
        return response

class HomeView(View):
    def get(self,request):
         if request.user.is_authenticated:
            return render(request, "authentication/HomePage.html")
         else:
            return HttpResponse("You need to log in to access this page.")

    
