from django.db import models

from products.models import Products
from sales_network.models.contacts import Contacts


class SalesNetwork(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Название сети продаж')
    contacts = models.OneToOneField(Contacts, on_delete=models.CASCADE, verbose_name='Контактная информация',
                                    related_name='sales_network_contacts')
    supplied_products = models.ManyToManyField(Products, verbose_name='Продукция торговой сети',
                                               related_name='sales_network_products')
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сеть продаж'
        verbose_name_plural = 'Сети продаж'
