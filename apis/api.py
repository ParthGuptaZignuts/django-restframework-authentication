from django.contrib import admin
from django.urls import path
from items.views import register_user,login_user,all_items,single_item,create_item,update_item,delete_item,change_password,request_password_reset,reset_password
from products.views import all_products,single_product,update_product,create_product,delete_product

urlpatterns = [
   path('register-user',register_user),
   path('login-user',login_user),
   path('all-items',all_items),
   path('single-item/<int:item_id>',single_item),
   path('create-item',create_item),
   path('update-item/<int:item_id>',update_item),
   path('delete-item/<int:item_id>',delete_item),
   path('change-password',change_password),
   path('request-password-reset', request_password_reset,name='request-password-reset'),
   path('reset-password/<uidb64>/<token>',reset_password,name='reset-password'),
   path('all-products',all_products, name='all_products'),
   path('products/<int:product_id>/',single_product, name='single_product'),
   path('products/create/',create_product, name='create_product'),
   path('products/update/<int:product_id>/',update_product, name='update_product'),
   path('products/delete/<int:product_id>/',delete_product, name='delete_product'),
]