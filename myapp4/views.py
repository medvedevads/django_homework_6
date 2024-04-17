from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, get_object_or_404


from myapp4.forms import ProductForm
from myapp4.models import Product

def update_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
    form = ProductForm(instance=product)
    context = {'product': product, 'form': form, 'title': 'Форма обновления данных товара'}
    return render(request, 'myapp4/order.html', context)

