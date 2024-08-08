from django.core.management.base import BaseCommand
from person.models import Person
from products.models import Products

class Command(BaseCommand):
    help = 'Seeds the database with initial data'

    def handle(self, *args, **kwargs):
        Person.objects.create(name='Admin User', role=Person.ADMIN)
        Person.objects.create(name='Regular User', role=Person.USER)
        
        Products.objects.create(
            product_name='Product 1',
            product_description='Description for product 1',
            product_price=9.99,
            product_stock=100
        )
        Products.objects.create(
            product_name='Product 2',
            product_description='Description for product 2',
            product_price=19.99,
            product_stock=50
        )
        
        self.stdout.write(self.style.SUCCESS('Database seeded successfully'))
