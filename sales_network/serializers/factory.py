from rest_framework import serializers

from sales_network.models.factory import Factory


class FactorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Factory
        fields = ['name', 'sales_network', 'contacts', 'supplied_products', 'created_at', 'is_active']
