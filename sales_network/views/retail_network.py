from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from sales_network.filters import RetailNetworkFilter
from sales_network.models.retail_network import RetailNetwork
from sales_network.serializers.retail_network import RetailNetworkSerializer


class RetailNetworkListAPIView(ListAPIView):
    queryset = RetailNetwork.objects.all()
    serializer_class = RetailNetworkSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = RetailNetworkFilter


class RetailNetworkCreateAPIView(CreateAPIView):
    serializer_class = RetailNetworkSerializer


class RetailNetworkDetailAPIView(RetrieveAPIView):
    queryset = RetailNetwork.objects.all()
    serializer_class = RetailNetworkSerializer


class RetailNetworkUpdateAPIView(UpdateAPIView):
    queryset = RetailNetwork.objects.all()
    serializer_class = RetailNetworkSerializer


class RetailNetworkDeleteAPIView(DestroyAPIView):
    queryset = RetailNetwork.objects.all()
    serializer_class = RetailNetworkSerializer
