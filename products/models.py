from django.db import models


# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название продукции')
    model = models.CharField(max_length=100, verbose_name='Модель')
    release_date = models.DateField(verbose_name='Дата выпуска')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукция'
        verbose_name_plural = 'Продукция'
