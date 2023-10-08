# Generated by Django 4.2.6 on 2023-10-05 18:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sales_network', '0003_retailnetwork'),
    ]

    operations = [
        migrations.AlterField(
            model_name='retailnetwork',
            name='factory_supplied',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='supplier', to='sales_network.factory', verbose_name='Поставщик оборудования'),
        ),
    ]
