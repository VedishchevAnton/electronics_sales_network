from django.db import models

from products.models import Products
from sales_network.models.contacts import Contacts
from sales_network.models.sales_network import SalesNetwork


class Factory(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Название фабрики')
    sales_network = models.ForeignKey(SalesNetwork, on_delete=models.CASCADE, verbose_name='Название сети продаж')
    contacts = models.OneToOneField(Contacts, on_delete=models.CASCADE, verbose_name='Контактная информация',
                                    related_name='factory_contacts')
    supplied_products = models.ManyToManyField(Products, verbose_name='Фабричная продукция',
                                               related_name='factory_products')
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Фабрика'
        verbose_name_plural = 'Фабрики'
