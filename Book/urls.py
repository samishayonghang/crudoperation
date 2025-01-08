from django.urls import path
from django.contrib import admin
from.views import Reviews,Genre,search,update,delete,loginpage,signup,logoutpage

urlpatterns = [
    path('', Reviews, name='reviews'),
    path('genre/',Genre , name='genre'),
    path('search/',search, name='search'),
    path('update/<int:pk>/',update, name='update'),
    path('delete/<int:pk>/',delete, name='delete'),
    path('search/',search, name='search'),
    path('login/',loginpage, name='loginpage'),
    path('signup/',signup, name='signup'),
    path('logout/',logoutpage, name='logoutpage'),
]




