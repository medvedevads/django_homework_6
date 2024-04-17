from random import randint
from django.utils.timezone import now
from django.core.management.base import BaseCommand
from myapp.models import Product, User, Order

class Command(BaseCommand):
    help = f'Создание Заказа по id Клиента и id Товара'

    def add_arguments(self, parser):
        parser.add_argument('customer_id', type=int, help='id клиента')

    def handle(self, *args, **options):
        customer_id = options.get('customer_id')

        order = Order(
            customer=User.objects.filter(pk=customer_id).first(),
            total_price=0,
            date_ordered=now(),
        )
        order.save()

        product = Product.objects.filter(pk=randint(1, 6)).first()
        order.products.add(product)
        order.total_price = product.price
        order.save()


        self.stdout.write(f'{order}')
