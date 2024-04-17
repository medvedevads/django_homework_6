from django.core.management.base import BaseCommand
from myapp4.models import Product



class Command(BaseCommand):
    help = "Generate fake goods."
    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Product ID')



    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            product = Product(name=f'Product{i}', description=f'This is unique goods {i}', price=i*10, quantity=i*5)
            product.save()
