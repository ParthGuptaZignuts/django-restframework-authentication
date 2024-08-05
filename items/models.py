from django.db import models

class Users(models.Model):
    username = models.CharField(max_length=20)
    email    = models.EmailField()
    password = models.CharField(max_length=20)

class Items(models.Model):
    item_name        = models.CharField(max_length=20)
    item_description = models.TextField()