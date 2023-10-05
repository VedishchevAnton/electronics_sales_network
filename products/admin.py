from django.contrib import admin
from django.contrib import admin

from products.models import Products


# Register your models here.
@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'model', 'release_date', 'is_active')
    list_filter = ('model', 'release_date', 'is_active',)
    search_fields = ('name',)
