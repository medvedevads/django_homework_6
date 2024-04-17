from django.contrib import admin
from myapp.models import User, Product, Order


@admin.action(description='Удалить адрес')
def update_address(modeladmin, request, queryset):
    queryset.update(address='')


@admin.action(description='Установить отсутствие')
def update_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'date_ordered']
    list_per_page = 10
    search_fields = ['id']
    fieldsets = [
        (
            'Клиент',
            {
                'fields': ['name'],
            },
        ),
        (
            'Подробности',
            {
                'fields': ['products'],
            },
        ),
        (
            'Стоимость заказа',
            {
                'fields': ['total_price']
            }
        ),
    ]



class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'quantity']
    ordering = ['date_added']
    list_per_page = 10
    search_fields = ['name']
    actions = [update_quantity]
    fieldsets = [
        (
            'Товар',
            {
                'fields': [('name', 'date_added')],
            },
        ),
        (
            'Подробности',
            {
                'fields': ['description'],
            },
        ),
        (
            'Стоимость и остаток',
            {
                'fields': ['price', 'quantity'],
            }
        ),
    ]



class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'address']
    ordering = ['date_registration']
    list_per_page = 10
    search_fields = ['phone']
    actions = [update_address]
    fieldsets = [
        (
            'Клиент',
            {
                'fields': [('name', 'phone')],
            },
        ),
        (
            'Подробности',
            {
                'fields': ['address'],
            },
        ),
        (
            'Контакты',
            {
                'fields': ['email'],
            }
        ),
        (
            'Прочее',
            {
                'description': 'Дополнительная информация',
                'fields': ['date_registration'],
            }
        ),
    ]

admin.site.register(User, UserAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
