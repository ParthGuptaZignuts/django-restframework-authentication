from django.core.management.base import BaseCommand
from faker import Faker
from authors.models import Author, Book
import random
import os

class Command(BaseCommand):
    help = 'Seed the database with Authors and Books'

    def handle(self, *args, **kwargs):
        fake = Faker()

        Author.objects.all().delete()
        Book.objects.all().delete()

        author_images = [f for f in os.listdir('media/authors/') if f.endswith(('.png', '.jpg', '.jpeg'))]
        book_images   = [f for f in os.listdir('media/books/') if f.endswith(('.png', '.jpg', '.jpeg'))]

        authors = []
        for _ in range(10):
            author = Author(
                name   = fake.name(),
                bio    = fake.text(),
                image  = f'authors/{random.choice(author_images)}'
            )
            author.save()
            authors.append(author)

        for _ in range(50):
            book = Book(
                book_title          = fake.catch_phrase(),
                book_description    = fake.text(),
                book_published_date = fake.date(),
                book_image          = f'books/{random.choice(book_images)}'  
            )
            book.save()
            book.book_author.add(*random.sample(authors, random.randint(1, 3)))

        self.stdout.write(self.style.SUCCESS('Successfully seeded the database with Authors and Books'))
