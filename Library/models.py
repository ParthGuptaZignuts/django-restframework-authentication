from django.db import models

class Library(models.Model):
    name     = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Book(models.Model):
    title   = models.CharField(max_length=255)
    author  = models.CharField(max_length=255)
    library = models.ForeignKey(Library, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


