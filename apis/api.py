from django.contrib import admin
from django.urls import path
from items.views import register_user,login_user

urlpatterns = [
   path('register-user',register_user),
   path('login-user',login_user)
]