# Generated by Django 4.2.6 on 2023-10-05 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название продукции')),
                ('model', models.CharField(max_length=100, verbose_name='Модель')),
                ('release_date', models.DateField(verbose_name='Дата выпуска')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Продукция',
                'verbose_name_plural': 'Продукция',
            },
        ),
    ]
