from django.db import models

class Person(models.Model):
    USER = 'user'
    ADMIN = 'admin'
    ROLE_CHOICES = [
        (USER, 'User'),
        (ADMIN, 'Admin'),
    ]

    name = models.CharField(max_length=100)
    role = models.CharField(max_length=5, choices=ROLE_CHOICES, default=USER)

    def __str__(self):
        return f"{self.name} ({self.role})"