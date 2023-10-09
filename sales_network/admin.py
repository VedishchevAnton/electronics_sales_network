from django.contrib import admin

from sales_network.models.contacts import Contacts
from sales_network.models.factory import Factory
from sales_network.models.individual_entrepreneur import IndividualEntrepreneur
from sales_network.models.retail_network import RetailNetwork
from sales_network.models.sales_network import SalesNetwork
from sales_network.admin_actions import clear_debt

from django.urls import reverse
from django.utils.html import format_html


# Register your models here.
@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'phone_number', 'country', 'city', 'street', 'house_number')
    list_filter = ('country', 'city')
    search_fields = ('email', 'phone_number',)


@admin.register(SalesNetwork)
class SalesNetworkAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'contacts', 'created_at', 'is_active', 'display_products')
    list_filter = ('name', 'contacts__city')
    search_fields = ('name',)

    # Функция для отображения продукции торговой сети
    def display_products(self, obj):
        return ", ".join([p.name for p in obj.supplied_products.all()])

    # Название для отображения функции в списке записей
    display_products.short_description = 'Продукция торговой сети'


@admin.register(Factory)
class FactoryAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'sales_network', 'contacts', 'created_at', 'is_active', 'display_products'
    )
    list_filter = ('name', 'sales_network__name', 'contacts__city')
    search_fields = ('name',)

    def display_products(self, obj):
        return ", ".join([p.name for p in obj.supplied_products.all()])

    display_products.short_description = 'Продукция торговой сети'


@admin.register(RetailNetwork)
class RetailNetworkAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'sales_network', 'contacts', 'display_factory_supplied', 'debt', 'created_at',
        'is_active', 'display_products'
    )
    list_filter = ('name', 'sales_network__name', 'contacts__city')
    search_fields = ('name',)
    actions = [clear_debt]

    def display_products(self, obj):
        return ", ".join([p.name for p in obj.supplied_products.all()])

    display_products.short_description = 'Продукция торговой сети'

    def display_factory_supplied(self, obj):
        if obj.factory_supplied:
            url = reverse("admin:sales_network_factory_change", args=[obj.factory_supplied.id])
            return format_html("<a href='{}'>{}</a>", url, obj.factory_supplied.name)
        else:
            return "-"

    display_factory_supplied.short_description = 'Поставщик оборудования'


@admin.register(IndividualEntrepreneur)
class IndividualEntrepreneurAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'sales_network', 'contacts', 'supplier', 'debt', 'created_at', 'is_active', 'display_products',
    )
    list_filter = ('name', 'sales_network__name', 'contacts__city')
    search_fields = ('name',)
    actions = [clear_debt]

    def display_products(self, obj):
        return ", ".join([p.name for p in obj.supplied_products.all()])

    display_products.short_description = 'Продукция торговой сети'

    def supplier(self, obj):
        # проверяем, выбран ли поставщик оборудования
        if obj.retail_network_supplied or obj.factory_supplied:
            # если выбран розничный поставщик, отображаем его название
            if obj.retail_network_supplied:
                supplier_obj = obj.retail_network_supplied
            # если выбран завод-поставщик, отображаем его название
            elif obj.factory_supplied:
                supplier_obj = obj.factory_supplied
            # если ни один поставщик не выбран, отображаем пустую строку
            else:
                return ''
            # создаем ссылку на объект поставщика
            url = reverse('admin:{}_{}_change'.format(
                supplier_obj._meta.app_label, supplier_obj._meta.model_name), args=[supplier_obj.pk])
            return format_html('<a href="{}">{}</a>', url, supplier_obj.name)
        # если поставщик не выбран, отображаем пустую строку
        else:
            return ''

    supplier.short_description = 'Поставщик оборудования'
