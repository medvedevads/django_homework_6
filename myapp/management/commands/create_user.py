from django.core.management.base import BaseCommand
import random
from myapp.models import User


class Command(BaseCommand):
    help = "Generate fake customer."
    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            user = User(name=f'Name{i}', email=f'mail{i}@mail.ru', phone=random.randint(79000000000,79999999999), address=f'{i} street, flat {i}')
            user.save()
