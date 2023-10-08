# Generated by Django 4.2.6 on 2023-10-05 18:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        ('sales_network', '0004_alter_retailnetwork_factory_supplied'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndividualEntrepreneur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Название ИП')),
                ('debt', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Задолженность перед поставщиком')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('contacts', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='individual_entrepreneur_contacts', to='sales_network.contacts', verbose_name='Контактная информация')),
                ('factory_supplied', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='factory_supplier', to='sales_network.factory', verbose_name='Поставщик оборудования')),
                ('retail_network_supplied', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='individual_entrepreneur_supplier', to='sales_network.retailnetwork', verbose_name='Поставщик оборудования')),
                ('sales_network', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales_network.salesnetwork', verbose_name='Название сети продаж')),
                ('supplied_products', models.ManyToManyField(related_name='individual_entrepreneur_products', to='products.products', verbose_name='Продукция торговой сети')),
            ],
            options={
                'verbose_name': 'Индивидуальный предприниматель',
                'verbose_name_plural': 'Индивидуальные предприниматели',
            },
        ),
    ]
