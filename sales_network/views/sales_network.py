from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from sales_network.models.sales_network import SalesNetwork
from sales_network.serializers.sales_network import SalesNetworkSerializer


class SalesNetworkListAPIView(ListAPIView):
    queryset = SalesNetwork.objects.all()
    serializer_class = SalesNetworkSerializer


class SalesNetworkCreateAPIView(CreateAPIView):
    serializer_class = SalesNetworkSerializer


class SalesNetworkDetailAPIView(RetrieveAPIView):
    queryset = SalesNetwork.objects.all()
    serializer_class = SalesNetworkSerializer


class SalesNetworkUpdateAPIView(UpdateAPIView):
    queryset = SalesNetwork.objects.all()
    serializer_class = SalesNetworkSerializer


class SalesNetworkDeleteAPIView(DestroyAPIView):
    queryset = SalesNetwork.objects.all()
    serializer_class = SalesNetworkSerializer
