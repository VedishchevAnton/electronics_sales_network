from django.contrib import admin

from sales_network.models.contacts import Contacts
from sales_network.models.factory import Factory


# Register your models here.

@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'phone_number', 'country', 'city', 'street', 'house_number')
    list_filter = ('country', 'city')
    search_fields = ('email', 'phone_number',)


@admin.register(Factory)
class FactoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'sales_network', 'contacts', 'created_at', 'is_active',)
    list_filter = ('name', 'sales_network',)
    search_fields = ('name',)

