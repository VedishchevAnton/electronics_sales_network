import django_filters

from sales_network.models.individual_entrepreneur import IndividualEntrepreneur
from sales_network.models.retail_network import RetailNetwork


class RetailNetworkFilter(django_filters.FilterSet):
    country = django_filters.CharFilter(field_name='contacts__country', lookup_expr='icontains')

    class Meta:
        model = RetailNetwork
        fields = ['country']


class IndividualEntrepreneurFilter(django_filters.FilterSet):
    country = django_filters.CharFilter(field_name='contacts__country', lookup_expr='icontains')

    class Meta:
        model = IndividualEntrepreneur
        fields = ['country']
