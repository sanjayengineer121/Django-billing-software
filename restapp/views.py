from rest_framework import generics
from .models import Student
from .serializers import StudentSerializer

# restapp/views.py

from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'pages-login.html')

def signup(request):
    return render(request, 'pages-register.html')

def contact(request):
    return render(request, 'pages-contact.html')

def profile(request):
    return render(request, 'users-profile.html')

def sales(request):
    return render(request, 'sales.html')

def reciept(request):
    return render(request, 'reciept.html')

def payment(request):
    return render(request, 'payment.html')

def saleereturn(request):
    return render(request, 'saleereturn.html')

def Purchase(request):
    return render(request, 'purchase.html')


class StudentListCreateView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
