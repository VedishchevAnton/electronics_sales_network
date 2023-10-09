from django.urls import path

from sales_network.views.factory import FactoryListAPIView, FactoryCreateAPIView, FactoryDetailAPIView, \
    FactoryUpdateAPIView, FactoryDeleteAPIView
from sales_network.views.individual_entrepreneur import IndividualEntrepreneurListAPIView, \
    IndividualEntrepreneurCreateAPIView, IndividualEntrepreneurDetailAPIView, IndividualEntrepreneurUpdateAPIView, \
    IndividualEntrepreneurDeleteAPIView
from sales_network.views.retail_network import RetailNetworkListAPIView, RetailNetworkCreateAPIView, \
    RetailNetworkDetailAPIView, RetailNetworkUpdateAPIView, RetailNetworkDeleteAPIView

urlpatterns = [
    path('factories/', FactoryListAPIView.as_view(), name='factory-list'),
    path('factories/create/', FactoryCreateAPIView.as_view(), name='factory-create'),
    path('factories/<int:pk>/', FactoryDetailAPIView.as_view(), name='factory-detail'),
    path('factories/<int:pk>/update/', FactoryUpdateAPIView.as_view(), name='factory-update'),
    path('factories/<int:pk>/delete/', FactoryDeleteAPIView.as_view(), name='factory-delete'),

    path('retail-networks/', RetailNetworkListAPIView.as_view(), name='retail-networks_list'),
    path('retail-networks/create/', RetailNetworkCreateAPIView.as_view(), name='retail-networks_create'),
    path('retail-networks/<int:pk>/', RetailNetworkDetailAPIView.as_view(), name='retail-networks_detail'),
    path('retail-networks/<int:pk>/update/', RetailNetworkUpdateAPIView.as_view(), name='retail-networks_update'),
    path('retail-networks/<int:pk>/delete/', RetailNetworkDeleteAPIView.as_view(), name='retail-networks_delete'),

    path('individual-entrepreneurs/', IndividualEntrepreneurListAPIView.as_view(), name='individual-entrepreneur-list'),
    path('individual-entrepreneurs/create/', IndividualEntrepreneurCreateAPIView.as_view(),
         name='individual-entrepreneur-create'),
    path('individual-entrepreneurs/<int:pk>/', IndividualEntrepreneurDetailAPIView.as_view(),
         name='individual-entrepreneur-detail'),
    path('individual-entrepreneurs/<int:pk>/update/', IndividualEntrepreneurUpdateAPIView.as_view(),
         name='individual-entrepreneur-update'),
    path('individual-entrepreneurs/<int:pk>/delete/', IndividualEntrepreneurDeleteAPIView.as_view(),
         name='individual-entrepreneur-delete'),
]
