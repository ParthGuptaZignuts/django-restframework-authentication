from django.contrib import admin
from django.urls import path
from items.views import register_user,login_user,all_items,single_item,create_item

urlpatterns = [
   path('register-user',register_user),
   path('login-user',login_user),
   path('all-items',all_items),
   path('single-item/<int:item_id>',single_item),
   path('create-item',create_item)
]