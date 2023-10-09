from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from sales_network.models.factory import Factory
from sales_network.serializers.factory import FactorySerializer


class FactoryListAPIView(ListAPIView):
    queryset = Factory.objects.all()
    serializer_class = FactorySerializer


class FactoryCreateAPIView(CreateAPIView):
    serializer_class = FactorySerializer


class FactoryDetailAPIView(RetrieveAPIView):
    queryset = Factory.objects.all()
    serializer_class = FactorySerializer


class FactoryUpdateAPIView(UpdateAPIView):
    queryset = Factory.objects.all()
    serializer_class = FactorySerializer


class FactoryDeleteAPIView(DestroyAPIView):
    queryset = Factory.objects.all()
    serializer_class = FactorySerializer
