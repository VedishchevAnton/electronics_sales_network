from django.urls import path

from products.views import ProductsList, ProductsDetail

urlpatterns = [
    path('products/', ProductsList.as_view(), name='products-list'),
    path('products/<int:pk>/', ProductsDetail.as_view(), name='products-detail'),
]
