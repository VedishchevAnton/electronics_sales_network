from rest_framework import serializers

from sales_network.models.contacts import Contacts


class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = ('email', 'phone_number', 'country', 'city', 'street', 'house_number')
