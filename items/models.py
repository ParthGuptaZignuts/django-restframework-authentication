from django.db import models

class Users(models.Model):
    USER = 'user'
    ADMIN = 'admin'
    ROLE_CHOICES = [
        (USER, 'User'),
        (ADMIN, 'Admin'),
    ]
    username = models.CharField(max_length=20)
    email    = models.EmailField()
    password = models.CharField(max_length=20)
    role     = models.CharField(max_length=5, choices=ROLE_CHOICES, default=USER)

class Items(models.Model):
    item_name        = models.CharField(max_length=20)
    item_description = models.TextField()