# urls.py

from django.urls import path
from .views import StudentListCreateView
from .views import index
from .views import login
from .views import signup
from .views import contact
from .views import profile
from .views import sales
from .views import payment
from .views import reciept
from .views import saleereturn
from .views import Purchase


# urls.py

from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('login/', login, name='login'),
    path('signup/',signup,name='signup'),
    path('contact/',contact,name='contact'),
    path('profile/',profile,name='profile'),
    path('sales/',sales,name='sales'),
    path('payment/',payment,name='payment'),
    path('reciept/',reciept,name='reciept'),
    path('saleereturn/',saleereturn,name='saleereturn'),
    path('Purchase/',Purchase,name='Purchase'),
    path('students/', StudentListCreateView.as_view(), name='student-list-create'),
    # Add more URLs for other views if needed
]
