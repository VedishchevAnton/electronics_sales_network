from django.urls import path

from sales_network.views.retail_network import RetailNetworkListAPIView, RetailNetworkCreateAPIView, \
    RetailNetworkDetailAPIView, RetailNetworkUpdateAPIView, RetailNetworkDeleteAPIView

urlpatterns = [
    path('retail-networks/', RetailNetworkListAPIView.as_view(), name='retail-networks_list'),
    path('retail-networks/create/', RetailNetworkCreateAPIView.as_view(), name='retail-networks_create'),
    path('retail-networks/<int:pk>/', RetailNetworkDetailAPIView.as_view(), name='retail-networks_detail'),
    path('retail-networks/<int:pk>/update/', RetailNetworkUpdateAPIView.as_view(), name='retail-networks_update'),
    path('retail-networks/<int:pk>/delete/', RetailNetworkDeleteAPIView.as_view(), name='retail-networks_delete'),
]
