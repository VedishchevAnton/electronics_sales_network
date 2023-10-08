from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from sales_network.models.individual_entrepreneur import IndividualEntrepreneur
from sales_network.serializers.individual_entrepreneur import IndividualEntrepreneurSerializer


class IndividualEntrepreneurListAPIView(ListAPIView):
    queryset = IndividualEntrepreneur.objects.all()
    serializer_class = IndividualEntrepreneurSerializer


class IndividualEntrepreneurCreateAPIView(CreateAPIView):
    serializer_class = IndividualEntrepreneurSerializer


class IndividualEntrepreneurDetailAPIView(RetrieveAPIView):
    queryset = IndividualEntrepreneur.objects.all()
    serializer_class = IndividualEntrepreneurSerializer


class IndividualEntrepreneurUpdateAPIView(UpdateAPIView):
    queryset = IndividualEntrepreneur.objects.all()
    serializer_class = IndividualEntrepreneurSerializer


class IndividualEntrepreneurDeleteAPIView(DestroyAPIView):
    queryset = IndividualEntrepreneur.objects.all()
    serializer_class = IndividualEntrepreneurSerializer
