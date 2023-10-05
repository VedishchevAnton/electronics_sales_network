from django.contrib import admin

from sales_network.models.contacts import Contacts
from sales_network.models.factory import Factory
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
    list_filter = ('name', )
    search_fields = ('name', )

    def display_products(self, obj):
        return ", ".join([p.name for p in obj.supplied_products.all()])

    display_products.short_description = 'Продукция торговой сети'


@admin.register(Factory)
class FactoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'sales_network', 'contacts', 'created_at', 'is_active', 'display_products')
    list_filter = ('name', 'sales_network')
    search_fields = ('name', )

    def display_products(self, obj):
        return ", ".join([p.name for p in obj.supplied_products.all()])

    display_products.short_description = 'Продукция торговой сети'


@admin.register(RetailNetwork)
class RetailNetworkAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'sales_network', 'contacts', 'factory_supplied', 'debt', 'created_at',
        'is_active', 'display_products'
    )
    list_filter = ('name', 'sales_network')
    search_fields = ('name',)

    def display_products(self, obj):
        return ", ".join([p.name for p in obj.supplied_products.all()])

    display_products.short_description = 'Продукция торговой сети'
