
from django.contrib import admin
from django.urls import include, path
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'pages-login.html')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('restapp.urls')),
    path('', include('restapp.urls'))
]
