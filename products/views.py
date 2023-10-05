from django.shortcuts import render
from rest_framework import generics
from .models import Products
from .serializers import ProductsSerializer


# Create your views here.
class ProductsList(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer


class ProductsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
