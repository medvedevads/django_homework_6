from django.core.management.base import BaseCommand
from random import randint
from myapp.models import User, Product, Order


class Command(BaseCommand):
    help = "Generate fake order."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        user = User.objects.filter(pk=pk).first()
        if user is not None:
            products = []
            common_price = 0
            for i in range(randint(1,5)):
                product = Product.objects.filter(pk=randint(1, 6)).first()
                common_price += product.price
                products.append(product)
            print(user)

            order = Order(customer=user, total_price=common_price)
            order.save()
            order.products.set(products)
