from django.urls import path

from sales_network.views.individual_entrepreneur import IndividualEntrepreneurListAPIView, \
    IndividualEntrepreneurCreateAPIView, IndividualEntrepreneurDetailAPIView, IndividualEntrepreneurUpdateAPIView, \
    IndividualEntrepreneurDeleteAPIView
from sales_network.views.retail_network import RetailNetworkListAPIView, RetailNetworkCreateAPIView, \
    RetailNetworkDetailAPIView, RetailNetworkUpdateAPIView, RetailNetworkDeleteAPIView

urlpatterns = [
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
