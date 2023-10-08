from django.contrib import admin

from sales_network.models.contacts import Contacts
from sales_network.models.factory import Factory
from sales_network.models.individual_entrepreneur import IndividualEntrepreneur
from sales_network.models.retail_network import RetailNetwork
from sales_network.models.sales_network import SalesNetwork


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

    def display_products(self, obj):
        return ", ".join([p.name for p in obj.supplied_products.all()])

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
        'id', 'name', 'sales_network', 'contacts', 'factory_supplied', 'debt', 'created_at',
        'is_active', 'display_products'
    )
    list_filter = ('name', 'sales_network__name', 'contacts__city')
    search_fields = ('name',)

    def display_products(self, obj):
        return ", ".join([p.name for p in obj.supplied_products.all()])

    display_products.short_description = 'Продукция торговой сети'


@admin.register(IndividualEntrepreneur)
class IndividualEntrepreneurAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'sales_network', 'contacts', 'supplier', 'debt', 'created_at', 'is_active', 'display_products',
    )
    list_filter = ('name', 'sales_network__name', 'contacts__city')
    search_fields = ('name',)

    def display_products(self, obj):
        return ", ".join([p.name for p in obj.supplied_products.all()])

    display_products.short_description = 'Продукция торговой сети'

    def supplier(self, obj):
        # проверяем, выбран ли поставщик оборудования
        if obj.retail_network_supplied or obj.factory_supplied:
            # если выбран розничный поставщик, отображаем его название
            if obj.retail_network_supplied:
                return obj.retail_network_supplied.name
            # если выбран завод-поставщик, отображаем его название
            elif obj.factory_supplied:
                return obj.factory_supplied.name
            # если ни один поставщик не выбран, отображаем пустую строку
            else:
                return ''
        # если поставщик не выбран, отображаем пустую строку
        else:
            return ''

    supplier.short_description = 'Поставщик оборудования'
