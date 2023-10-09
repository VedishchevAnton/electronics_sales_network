from rest_framework import serializers

from sales_network.models.sales_network import SalesNetwork


class SalesNetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesNetwork
        fields = ['name', 'contacts', 'supplied_products', 'created_at', 'is_active']

