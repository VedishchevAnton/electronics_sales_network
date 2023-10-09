from rest_framework import serializers
from products.models import Products


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('id', 'name', 'model', 'release_date', 'is_active')
