from rest_framework import serializers

from sales_network.models.individual_entrepreneur import IndividualEntrepreneur


class IndividualEntrepreneurSerializer(serializers.ModelSerializer):
    debt = serializers.ReadOnlyField()

    class Meta:
        model = IndividualEntrepreneur
        fields = ['id', 'name', 'sales_network', 'contacts', 'supplied_products', 'retail_network_supplied',
                  'factory_supplied', 'debt', 'created_at', 'is_active']
