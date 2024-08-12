from django.contrib import admin
from django.urls import path
from items.views import register_user,login_user,all_items,single_item,create_item,update_item,delete_item,change_password,request_password_reset,reset_password
from products.views import all_products,single_product,update_product,create_product,delete_product
from Library.views import all_libraries,single_library,create_library,update_library,delete_library,all_books,single_book,create_book,update_book,delete_book
from authors.views import all_authors , create_author , single_author , update_author , delete_author

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
   path('libraries/',all_libraries, name='all_libraries'),
   path('libraries/<int:library_id>/',single_library, name='single_library'),
   path('libraries/create/',create_library, name='create_library'),
   path('libraries/update/<int:library_id>/',update_library, name='update_library'),
   path('libraries/delete/<int:library_id>/',delete_library, name='delete_library'),
   path('books/',all_books, name='all_books'),
   path('books/<int:book_id>/',single_book, name='single_book'),
   path('books/create/',create_book, name='create_book'),
   path('books/update/<int:book_id>/',update_book, name='update_book'),
   path('books/delete/<int:book_id>/',delete_book, name='delete_book'),

   path('authors',all_authors, name = "authors"),
   path('author/<int:author_id>',single_author, name = "single_author"),
   path('create_author',create_author , name = "create_author"),
   path('update_author/<int:author_id>',update_author, name = "update_author"),
   path('delete_author/<int:author_id>',delete_author, name = "delete_author"),
   
]