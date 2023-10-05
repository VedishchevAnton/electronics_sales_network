from django.db import models
from rest_framework.exceptions import ValidationError

from products.models import Products
from sales_network.models.contacts import Contacts
from sales_network.models.factory import Factory
from sales_network.models.retail_network import RetailNetwork
from sales_network.models.sales_network import SalesNetwork

NULLABLE = {'blank': True, 'null': True}


class IndividualEntrepreneur(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Название ИП')
    sales_network = models.ForeignKey(SalesNetwork, on_delete=models.CASCADE, verbose_name='Название сети продаж')
    contacts = models.OneToOneField(Contacts, on_delete=models.CASCADE, verbose_name='Контактная информация',
                                    related_name='individual_entrepreneur_contacts')
    supplied_products = models.ManyToManyField(Products, verbose_name='Продукция торговой сети',
                                               related_name='individual_entrepreneur_products')
    retail_network_supplied = models.OneToOneField(RetailNetwork, on_delete=models.SET_NULL,
                                                   verbose_name='Поставщик оборудования(розница)',
                                                   related_name='individual_entrepreneur_supplier', **NULLABLE)
    factory_supplied = models.OneToOneField(Factory, on_delete=models.SET_NULL,
                                            verbose_name='Поставщик оборудования(завод)',
                                            related_name='factory_supplier', **NULLABLE)
    debt = models.DecimalField(max_digits=10, decimal_places=2, default=0,
                               verbose_name='Задолженность перед поставщиком')
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'ИП {self.name}'

    def clean(self):
        # проверяем, что только одно из полей заполнено
        if self.retail_network_supplied and self.factory_supplied:
            raise ValidationError('Можно выбрать только одного поставщика оборудования!')

    def save(self, *args, **kwargs):
        # сохраняет объект в базу данных, если проверка прошла успешно
        self.clean()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Индивидуальный предприниматель'
        verbose_name_plural = 'Индивидуальные предприниматели'
