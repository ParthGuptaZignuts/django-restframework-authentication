from django.core.management.base import BaseCommand
from faker import Faker
from Library.models import Library, Book
import random

class Command(BaseCommand):
    help = 'Seed the database with Libraries and Books'

    def handle(self, *args, **kwargs):
        fake = Faker()

        Library.objects.all().delete()
        Book.objects.all().delete()

        libraries = []
        for _ in range(10): 
            library = Library(
                name=fake.company(),
                location=fake.address()
            )
            library.save()
            libraries.append(library)

        for _ in range(50): 
            book = Book(
                title=fake.catch_phrase(),
                author=fake.name(),
                library=random.choice(libraries)
            )
            book.save()

        self.stdout.write(self.style.SUCCESS('Successfully seeded the database with Libraries and Books'))
