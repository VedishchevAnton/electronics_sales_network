import django_filters

from sales_network.models.retail_network import RetailNetwork


class CountryFilter(django_filters.FilterSet):
    country = django_filters.CharFilter(field_name='contacts__country', lookup_expr='icontains')

    class Meta:
        model = RetailNetwork
        fields = ['country']
