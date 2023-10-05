from django.db import models

from products.models import Products
from sales_network.models.contacts import Contacts
from sales_network.models.factory import Factory
from sales_network.models.sales_network import SalesNetwork


class RetailNetwork(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Название розничной сети')
    sales_network = models.ForeignKey(SalesNetwork, on_delete=models.CASCADE, verbose_name='Название сети продаж')
    contacts = models.OneToOneField(Contacts, on_delete=models.CASCADE, verbose_name='Контактная информация',
                                    related_name='retail_network_contacts')
    supplied_products = models.ManyToManyField(Products, verbose_name='Продукция торговой сети',
                                               related_name='retail_network_products')
    factory_supplied = models.ForeignKey(Factory, on_delete=models.SET_NULL, null=True,
                                         verbose_name='Поставщик оборудования',
                                         related_name='supplier')
    debt = models.DecimalField(max_digits=10, decimal_places=2, default=0,
                               verbose_name='Задолженность перед поставщиком')
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Розничная сеть'
        verbose_name_plural = 'Розничные сети'
