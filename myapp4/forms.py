
from django.forms import ModelForm, Textarea

from myapp4.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = [
            'name',
            'description',
            'price',
            'quantity',
            'image',
        ]
        widgets = {
            'description': Textarea(attrs={'class': 'form-control', 'placeholder': f'Описание товара..'})
        }
        labels = {
            'name': 'Наименование',
            'description': '',
            'price': 'Цена',
            'quantity': 'Количество',
            'image': 'Изображение',
        }