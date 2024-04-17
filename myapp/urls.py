from django.urls import path
from .views import index, about, order
from . import views

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('order/<int:customer_id>/', views.order, name='order'),
    path('double/<int:customer_id>/<int:scope_in_days>/', views.double, name='double'),
]