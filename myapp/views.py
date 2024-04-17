from django.shortcuts import render, get_object_or_404
import logging
from .models import User, Order
from datetime import timedelta
from django.utils import timezone

logger = logging.getLogger(__name__)

def index(request):
    logger.info('Index page accessed')
    return render(request, "myapp/index.html")

def about(request):
    logger.info('About page accessed')
    return render(request, "myapp/about.html")

def order(request, customer_id):
    customer = get_object_or_404(User, pk=customer_id)
    orders = Order.objects.filter(customer=customer).all()
    context = {'customer': customer, 'orders': orders}
    return render(request, 'myapp/order.html', context)


def double(request, customer_id, scope_in_days=365):
    scope_dict = {}
    if scope_in_days not in (7, 30, 365):
        scope_dict.setdefault(f'{scope_in_days}', [])
    else:
        scope_dict.update({'7': [], '30': [], '365': []})

    customer = get_object_or_404(User, pk=customer_id)
    context = {'customer': customer}

    for k, v in scope_dict.items():
        orders = Order.objects.filter(customer=customer, date_ordered__gte=timezone.now() - timedelta(days=int(k)))
        products = set()
        for order in orders:
            products.update(order.products.all())

        products = list(products)
        products.sort(key=lambda x: x.price, reverse=True)
        scope_dict[k].extend(products)

    context['scope_dict'] = scope_dict

    return render(request, 'myapp/double.html', context)