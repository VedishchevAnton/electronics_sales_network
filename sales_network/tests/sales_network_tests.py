from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

from sales_network.models.contacts import Contacts
from sales_network.models.sales_network import SalesNetwork


class SalesNetworkTests(APITestCase):
    def setUp(self):
        self.contacts = Contacts.objects.create(
            email='test@example.com',
            phone_number='+71234567891',
            country='USA',
            city='New York',
            street='Broadway',
            house_number='123'
        )
        self.sales_network = SalesNetwork.objects.create(
            name='Test Sales Network',
            contacts=self.contacts,
            is_active=True
        )

    def test_get_sales_network_list(self):
        url = reverse('sales-network-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_sales_network(self):
        url = reverse('sales-network-create')
        data = {
            'name': 'New Sales Network',
            'contacts': {
                'email': 'new@example.com',
                'phone_number': '+7234567890',
                'country': 'USA',
                'city': 'New York',
                'street': 'Broadway',
                'house_number': '123'
            },
            'is_active': True
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(SalesNetwork.objects.count(), 2)
