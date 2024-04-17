from django.urls import path
from .views import update_product
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('update_product/<int:product_id>/', update_product, name='update_product'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
