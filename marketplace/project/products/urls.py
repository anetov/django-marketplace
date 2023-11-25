from django.urls import path
from django.contrib.auth.decorators import login_required
from products.views import CreateProduct, ProductDetail, delete, edit, products


app_name = 'product'

urlpatterns = [
    path('', products, name='products'),
    path('create_product/', login_required(CreateProduct.as_view()), name='create_product'),
    path('<int:pk>/', ProductDetail.as_view(), name='detail'),
    path('<int:pk>/delete/', delete, name='delete'),
    path('<int:pk>/edit/', edit, name='edit'),
]