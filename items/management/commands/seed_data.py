from django.core.management.base import BaseCommand
from faker import Faker
from items.models import Items 

class Command(BaseCommand):
    help = "Seeds the database with the fake data using Faker"

    def handle(self , *args, **kwargs):
        fake = Faker()

        for _ in range(10): 
            Items.objects.create(
                item_name=fake.name(),
                item_description=fake.text(),
            )

        self.stdout.write(self.style.SUCCESS('Database seeded with fake data successfully for items'))