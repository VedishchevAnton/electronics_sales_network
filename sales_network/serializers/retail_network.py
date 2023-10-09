from rest_framework import serializers

from sales_network.models.retail_network import RetailNetwork


class RetailNetworkSerializer(serializers.ModelSerializer):
    debt = serializers.ReadOnlyField()

    class Meta:
        model = RetailNetwork
        fields = ['id', 'name', 'sales_network', 'contacts', 'supplied_products', 'factory_supplied', 'debt',
                  'created_at', 'is_active']