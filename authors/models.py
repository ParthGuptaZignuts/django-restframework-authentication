from django.db import models

class Author(models.Model):
    name  = models.CharField(max_length=100)
    bio   = models.TextField()
    image = models.ImageField(upload_to='authors/', null=True, blank=True)

    def __str__(self):
        return self.name

class Book(models.Model):  
    book_title          = models.CharField(max_length=100)
    book_description    = models.TextField()
    book_author         = models.ManyToManyField(Author, related_name='books')
    book_published_date = models.DateField()
    book_image          = models.ImageField(upload_to='books/', null=True, blank=True)

    def __str__(self):
        return self.book_title
