from django.contrib import admin
from .models import Category, Product
# from .forms import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'category', 'price', 'available', 'created', 'updated']
    list_filter = ['available', 'category', 'created', 'price']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}


# admin.site.register()
