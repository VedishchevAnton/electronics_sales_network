from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Contacts(models.Model):
    email = models.EmailField(unique=True, verbose_name='Электронная почта')
    phone_number = PhoneNumberField(unique=True, verbose_name='Номер телефона')  # формат E.164
    country = models.CharField(max_length=50, verbose_name='Страна')
    city = models.CharField(max_length=50, verbose_name='Город')
    street = models.CharField(max_length=100, verbose_name='Улица')
    house_number = models.CharField(max_length=200, verbose_name='Номер дома')

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Контактная информация'
        verbose_name_plural = 'Контактная информация'
